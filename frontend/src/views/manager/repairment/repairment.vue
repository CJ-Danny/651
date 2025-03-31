<template>
  <div style="margin-left: 6vw;margin-top:30px">
    <div style="display: flex">
      <div style="background-color: #FBFBFB;width:35vw;height:50px;display: flex;align-items: center">
        <div style="background-color: #0d9fda;width:10px;height:50px"></div>
        <div style="padding-left: 25px">Welcome! Please process all current maintenance orders within one hour.</div>
      </div>
    </div>
    <div style="float:right;margin-right: 50px;margin-top: -70px"><img src="../../../assets/repair/logo.png"></div>

    <div>
      <div>
        <el-table
            :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            :row-class-name="setTimeOut"
            style="width: 95%"
            v-loading="isLoading"
            >
          <!-- Sequential Number -->
          <el-table-column
              label="#"
              type="index"
              width="60"
              align="center"
              :index="sequentialIndex">
          </el-table-column>
          
          <!-- Submission Time -->
          <el-table-column
              prop="submitTime"
              label="Submission Time"
              width="160"
              sortable>
              <template slot-scope="scope">
                {{ formatDateTime(scope.row.submitTime) }}
              </template>
          </el-table-column>
          
          <!-- Assignment Time - Added column -->
          <el-table-column
              prop="assignTime"
              label="Assignment Time"
              width="160"
              sortable>
              <template slot-scope="scope">
                {{ formatDateTime(scope.row.assignTime) }}
              </template>
          </el-table-column>
          
          <!-- Finish Time - Show only on completed orders page -->
          <el-table-column
              v-if="$route.query.type === '1'"
              prop="finishTime"
              label="Finish Time"
              width="160"
              sortable>
              <template slot-scope="scope">
                {{ formatDateTime(scope.row.finishTime) }}
              </template>
          </el-table-column>
          
          <!-- Room Number -->
          <el-table-column
              prop="roomNumber"
              label="Room Number"
              width="120"
              align="center">
          </el-table-column>
          
          <!-- Description -->
          <el-table-column
              prop="description"
              label="Description"
              min-width="200"
              align="center">
          </el-table-column>
          
          <!-- Solution - Show only on completed orders page -->
          <el-table-column
              v-if="$route.query.type === '1'"
              prop="method"
              label="Solution"
              min-width="200"
              align="center">
          </el-table-column>
          
          <!-- Repairman -->
          <el-table-column
              prop="repairmanName"
              label="Repairman"
              width="120"
              align="center">
          </el-table-column>
          
          <!-- Repairman Email -->
          <el-table-column
              prop="repairmanEmail"
              label="Repairman Email"
              width="180"
              align="center">
          </el-table-column>
          
          <!-- Operations -->
          <el-table-column
                label="Operations"
                width="180"
                align="center">
            <template v-slot="scope">
                <div class="operations-container">
                <div v-if="scope.row.status===0 && $store.state.userType===1">
                    <el-button type="primary" size="small" class="operation-button" @click="openDialog(scope.row.orderID, scope.row.description)">Assign</el-button>
                </div>
                <div v-else-if="scope.row.status===1 && $store.state.userType===2" class="status-with-button">
                    <div class="status-tag-container">
                      <el-tag type="warning">In Progress</el-tag>
                    </div>
                    <el-button type="success" size="small" class="operation-button" @click="openWorkerDialog(scope.row.orderID)">Complete</el-button>
                </div>
                <div v-else-if="scope.row.status===1">
                    <div class="status-tag-container">
                      <el-tag type="warning">In Progress</el-tag>
                    </div>
                </div>
                <div v-else-if="scope.row.status===2 && $store.state.userType===1" class="status-with-button">
                    <div class="status-tag-container">
                      <el-tag type="success">Completed</el-tag>
                    </div>
                    <el-button type="warning" size="small" class="operation-button" @click="addToKnowledgeBase(scope.row)" 
                              v-if="!scope.row.addedToKnowledge">Add to Knowledge</el-button>
                    <div class="status-tag-container" v-else>
                      <el-tag type="info">Added to KB</el-tag>
                    </div>
                </div>
                <div v-else-if="scope.row.status===2">
                    <div class="status-tag-container">
                      <el-tag type="success">Completed</el-tag>
                    </div>
                </div>
                <div v-else-if="scope.row.status===3">
                    <div class="status-tag-container">
                      <el-tag type="danger">Error</el-tag>
                    </div>
                </div>
                <div v-else>
                    <div class="status-tag-container">
                      <el-tag type="info">Not Assigned</el-tag>
                    </div>
                </div>
                </div>
            </template>
            </el-table-column>
        </el-table>

        <div class="pageDiv">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[5,10, 15, 20]"
              :page-size="10"
              layout="total, sizes, prev, pager, next, jumper"
              :total="this.tableData.length">
          </el-pagination>
        </div>

        <!-- Worker Dialog for completing an order -->
        <div>
          <el-dialog title="Maintenance Report" :visible.sync="dialogFormVis2">
            <el-input
                type="textarea"
                :rows="5"
                placeholder="Please enter solution details"
                v-model="solveMethod">
            </el-input>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVis2 = false">Cancel</el-button>
                <el-button type="primary" @click="submitSolution">Submit</el-button>
            </div>
          </el-dialog>
        </div>

        <!-- Assign Dialog for assigning repairman -->
        <div>
          <el-dialog title="Assign Repairman" :visible.sync="dialogFormVisible" width="75%" top="2%">
            <el-form :model="form">
              <el-form-item label="Issue Description: " :label-width="formLabelWidth">
                <div>{{this.tempDescription}}</div>
              </el-form-item>

              <el-form-item label="Select Repairman: " :label-width="formLabelWidth">
                <div>
                  <el-table
                      ref="singleTable"
                      :data="workerData"
                      style="width: 100%;">
                    <el-table-column
                        width="55">
                      <template slot-scope="scope">
                        <el-radio 
                          :label="scope.row.managerId" 
                          v-model="form.managerID"
                          @change="handleRadioChange(scope.row)">
                        </el-radio>
                      </template>
                    </el-table-column>
                    <el-table-column
                        property="name"
                        label="Name"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="email"
                        label="Email"
                        width="180">
                    </el-table-column>
                    <el-table-column
                        property="type"
                        label="Type"
                        width="120">
                      <template v-slot="scope">
                        <div v-if="scope.row.type===1">Admin</div>
                        <div v-else-if="scope.row.type===2">Plumber</div>
                        <div v-else-if="scope.row.type===3">Electrician</div>
                        <div v-else-if="scope.row.type===4">Mechanic</div>
                      </template>
                    </el-table-column>
                    <el-table-column
                        label="Workload"
                        width="150">
                      <template v-slot="scope">
                        <div>Finished: {{scope.row.finished_num}}</div>
                        <div>Pending: {{scope.row.unfinished_num}}</div>
                      </template>
                    </el-table-column>
                  </el-table>
                </div>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">Cancel</el-button>
              <el-button type="primary" @click="assignRepairman">Confirm</el-button>
            </div>
          </el-dialog>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "repairment",

  data() {
    return {
      tempDescription: '',
      isLoading: true,
      solveMethod: null,
      dialogFormVis2: false,
      fixID: null,
      currentPage: 1,
      pageSize: 10,
      workerData: [],
      tableData: [],
      dialogFormVisible: false,
      form: {
        managerID: null,
        orderID: null,
      },
      formLabelWidth: '180px',
      addedToKnowledgeList: [], // Track which orders have been added to KB
    }
  },

  created() {
    this.loadRepairmen();
    this.loadOrders();
  },

  watch: {
    '$route.query.type': {
      handler() {
        this.tableData = [];
        this.isLoading = true;
        this.loadOrders();
      },
      deep: true
    }
  },

  methods: {
    // Method for sequential index calculation
    sequentialIndex(index) {
      return (this.currentPage - 1) * this.pageSize + index + 1;
    },
    
    // Simple timeout check method
    setTimeOut(row) {
      // You can implement logic to highlight rows based on time criteria
      return ''; // Default empty class
    },

    formatDateTime(dateString) {
      if (!dateString || dateString.includes('2000-01-01')) return '—';
      const date = new Date(dateString);
      return date.toLocaleString();
    },
    
    // Load repairmen for assignment
    loadRepairmen() {
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      
      this.$axios({
        method: 'post',
        url: '/manager/getManagerInfo',
        data: formData
      })
      .then((res) => {
        if (res.data.errno === 0) {
          this.workerData = res.data.data;
        } else {
          console.log(res.data);
        }
      })
      .catch((err) => {
        console.log(err);
      });
    },

    // Load orders based on route type and user type
    loadOrders() {
      this.isLoading = true;
      const formData = new FormData();
      formData.append("token", this.$store.state.token);
      formData.append("type", this.$route.query.type || '0');
      formData.append("isUser", this.$store.state.userState);
      
      // Get user type and ID from store
      const userType = this.$store.state.userType || 1; // Default to manager type if undefined
      const userID = this.$store.state.adminID; // Use adminID from the store
      
      // Select API endpoint based on user type
      let url = '/service/getAllOrders'; // Default for managers
      
      // Only use repairman-specific endpoint if user is a repairman and has an ID
      if (userType === 2 && userID) {
        url = '/service/getManagerOrder';
        formData.append("managerID", userID);
      }
      
      this.$axios({
        method: 'post',
        url: url,
        data: formData
      })
      .then((res) => {
        if (res.data.errno === 0) {
          // Filter orders based on current tab
          let filteredOrders = res.data.data || [];
          const type = this.$route.query.type || '0';
          
          if (type === '0') {
            // Pending tab - only show orders with status 0 (not distributed) or 1 (in progress)
            filteredOrders = filteredOrders.filter(order => order.status === 0 || order.status === 1);
          } else if (type === '1') {
            // Completed tab - only show orders with status 2 (finished) or 3 (error)
            filteredOrders = filteredOrders.filter(order => order.status === 2 || order.status === 3);
          }
          
          // Additional filtering for repairmen if we used the getAllOrders endpoint
          if (userType === 2 && url === '/service/getAllOrders' && userID) {
            filteredOrders = filteredOrders.filter(order => order.managerID === userID);
          }
          
          // Process data to include additional repairman information
          this.tableData = this.processOrderData(filteredOrders);
          
          // Sort orders by orderID to ensure consistent sequencing
          this.tableData.sort((a, b) => a.orderID - b.orderID);
        } else {
          console.log("API Error:", res.data);
          this.$message.error("Failed to load orders: " + (res.data.errmsg || "Unknown error"));
          this.tableData = [];
        }
        this.isLoading = false;
      })
      .catch((err) => {
        console.log("API Error:", err);
        
        // If the getManagerOrder endpoint fails, fall back to getAllOrders
        if (url === '/service/getManagerOrder') {
          console.log("Falling back to getAllOrders endpoint");
          
          // Remove the managerID parameter if it was set
          const newFormData = new FormData();
          for (let pair of formData.entries()) {
            if (pair[0] !== 'managerID') {
              newFormData.append(pair[0], pair[1]);
            }
          }
          
          this.$axios({
            method: 'post',
            url: '/service/getAllOrders',
            data: newFormData
          })
          .then((res) => {
            if (res.data.errno === 0) {
              // Filter by status
              let fallbackOrders = res.data.data || [];
              const type = this.$route.query.type || '0';
              
              if (type === '0') {
                fallbackOrders = fallbackOrders.filter(order => order.status === 0 || order.status === 1);
              } else if (type === '1') {
                fallbackOrders = fallbackOrders.filter(order => order.status === 2 || order.status === 3);
              }
              
              // Filter by managerID for repairmen
              if (userType === 2 && userID) {
                fallbackOrders = fallbackOrders.filter(order => order.managerID === userID);
              }
              
              this.tableData = this.processOrderData(fallbackOrders);
              
              // Sort orders by orderID to ensure consistent sequencing
              this.tableData.sort((a, b) => a.orderID - b.orderID);
            } else {
              this.$message.error("Failed to load orders: " + (res.data.errmsg || "Unknown error"));
              this.tableData = [];
            }
            this.isLoading = false;
          })
          .catch((fallbackErr) => {
            console.error("Fallback API Error:", fallbackErr);
            this.$message.error("Failed to load orders. Please try again later.");
            this.tableData = [];
            this.isLoading = false;
          });
        } else {
          this.$message.error("Failed to load orders. Please try again later.");
          this.tableData = [];
          this.isLoading = false;
        }
      });
    },

    // Process order data to include repairman information only
    processOrderData(orders) {
      return orders.map(order => {
        let repairmanName = 'Not assigned';
        let repairmanEmail = '—';
        
        // If there's a valid managerID, find matching repairman data
        if (order.managerID > 0 && this.workerData.length > 0) {
          const repairman = this.workerData.find(worker => worker.managerId === order.managerID);
          if (repairman) {
            repairmanName = repairman.name;
            repairmanEmail = repairman.email;
          } else {
            repairmanName = `Repairman ${order.managerID}`;
            repairmanEmail = 'Email unavailable';
          }
        }
        
        // Check if this order has been added to knowledge base
        const addedToKnowledge = this.addedToKnowledgeList.includes(order.orderID);
        
        return {
          ...order,
          repairmanName: repairmanName,
          repairmanEmail: repairmanEmail,
          addedToKnowledge: addedToKnowledge
        };
      });
    },

    handleSizeChange(val) {
      this.pageSize = val;
    },
    
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    
    handleRadioChange(row) {
      this.currentRow = row;
      // managerID is already set by v-model on the radio button
    },
    
    openDialog(ID, des) {
      this.dialogFormVisible = true;
      this.form.orderID = ID;
      this.tempDescription = des;
    },
    
    openWorkerDialog(ID) {
      this.dialogFormVis2 = true;
      this.fixID = ID;
    },
    
    // Assign repairman to the order
    assignRepairman() {
      if (!this.form.managerID) {
        this.$message.warning("Please select a repairman");
        return;
      }

      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.form.orderID);
      formData.append("managerID", this.form.managerID);
      
      this.$axios({
        method: 'post',
        url: '/service/assainOrder',
        data: formData
      })
      .then((res) => {
        this.dialogFormVisible = false;
        if (res.data.errno === 0) {
          this.$message.success("Order assigned successfully");
          this.loadOrders();
        } else {
          this.$message.error("Failed to assign order");
          console.log(res.data);
        }
      })
      .catch((err) => {
        console.log(err);
      });
    },

    // Submit solution for the order
    submitSolution() {
      if (!this.solveMethod) {
        this.$message.warning("Please enter solution details");
        return;
      }
      
      const formData = new FormData();
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.fixID);
      formData.append("method", this.solveMethod);
      
      this.$axios({
        method: 'post',
        url: '/service/finishOrder',
        data: formData
      })
      .then((res) => {
        if (res.data.errno === 0) {
          this.dialogFormVis2 = false;
          this.$message.success("Order completed successfully");
          this.loadOrders();
        } else {
          this.$message.error("Failed to complete order: " + (res.data.errmsg || "Unknown error"));
        }
      })
      .catch((err) => {
        console.error("Error details:", err);
        this.$message.error("Server error when completing order");
      });
    },

    // Add to knowledge base
    addToKnowledgeBase(row) {
      // Check if we have the necessary data
      if (!row.description || !row.method) {
        this.$message.warning("Missing problem description or solution method");
        return;
      }
      
      const knowledgeData = new FormData();
      knowledgeData.append("token", this.$store.state.token);
      knowledgeData.append("problem", row.description);
      knowledgeData.append("solution", row.method);
      
      // Show loading message
      const loadingMessage = this.$message({
        message: 'Adding to knowledge base...',
        type: 'info',
        duration: 0
      });
      
      this.$axios({
        method: 'post',
        url: '/manager/addKnowledge',
        data: knowledgeData
      })
      .then((res) => {
        // Close loading message
        loadingMessage.close();
        
        if (res.data.errno === 0) {
          this.$message.success("Solution added to knowledge base");
          
          // Add to our local tracked list of orders added to KB
          this.addedToKnowledgeList.push(row.orderID);
          
          // Update the table row to show it's been added
          const index = this.tableData.findIndex(item => item.orderID === row.orderID);
          if (index !== -1) {
            this.$set(this.tableData[index], 'addedToKnowledge', true);
          }
        } else {
          this.$message.error("Failed to add to knowledge base: " + (res.data.errmsg || "Unknown error"));
        }
      })
      .catch((err) => {
        // Close loading message
        loadingMessage.close();
        
        console.error("Error adding to knowledge base:", err);
        this.$message.error("Server error when adding to knowledge base");
      });
    }
  }
}
</script>

<style scoped>
.pageDiv {
  padding-top: 30px;
  text-align: center;
  padding-bottom: 50px;
}

.status-tag-container {
  display: flex;
  justify-content: center;
  width: 100%;
}

.status-tag-container .el-tag {
  width: 140px;
  text-align: center;
  display: inline-block;
  padding: 8px 0;
  height: auto;
  line-height: 1.5;
}

.operation-button {
  width: 140px;
  margin: 0 auto;
  padding: 8px 0;
  height: auto;
  line-height: 1.5;
}

.el-button--warning {
  background-color: #F8C037; /* Yellow color */
  border-color: #E6A23C;
}

.status-with-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.operations-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

<style>
.el-table .warning-row {
  background: rgba(245,108,108, 0.12);
}

.el-table .stripe-row {
  background: rgb(250,250,250);
}
</style>