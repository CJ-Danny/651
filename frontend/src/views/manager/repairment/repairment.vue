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
          <!-- Order Number -->
          <el-table-column
              prop="orderID"
              label="Order #"
              width="80"
              align="center">
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
                    <el-button type="primary" size="small" @click="openDialog(scope.row.orderID, scope.row.description)">Assign</el-button>
                </div>
                <div v-else-if="scope.row.status===1 && $store.state.userType===2" class="status-with-button">
                    <el-tag type="warning">In Progress</el-tag>
                    <el-button type="success" size="small" @click="openWorkerDialog(scope.row.orderID)">Complete</el-button>
                </div>
                <div v-else-if="scope.row.status===1">
                    <el-tag type="warning">In Progress</el-tag>
                </div>
                <div v-else-if="scope.row.status===2">
                    <el-tag type="success">Completed</el-tag>
                </div>
                <div v-else-if="scope.row.status===3">
                    <el-tag type="danger">Error</el-tag>
                </div>
                <div v-else>
                    <el-tag type="info">Not Assigned</el-tag>
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
          <el-dialog title="Assign Repairman" :visible.sync="dialogFormVisible" width="65%" top="2%">
            <el-form :model="form">
              <el-form-item label="Issue Description" :label-width="formLabelWidth">
                <div>{{this.tempDescription}}</div>
              </el-form-item>

              <el-form-item label="Select Repairman" :label-width="formLabelWidth">
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

              <el-form-item label="Schedule" :label-width="formLabelWidth" style="margin-top: 20px">
                <el-date-picker
                    v-model="dateValue"
                    value-format="yyyy-MM-dd"
                    align="right"
                    type="date"
                    placeholder="Select date"
                    :picker-options="pickerOptions">
                </el-date-picker>
                <el-time-select
                    style="margin-left: 20px"
                    placeholder="Start time"
                    v-model="startTime"
                    value-format="HH:mm:ss"
                    :picker-options="{
                    start: '08:30',
                    step: '00:15',
                    end: '18:30'
                  }">
                </el-time-select>
                <el-time-select
                    style="margin-left: 20px"
                    placeholder="End time"
                    value-format="HH:mm:ss"
                    v-model="endTime"
                    :picker-options="{
                    start: '08:30',
                    step: '00:15',
                    end: '18:30',
                    minTime: startTime
                  }">
                </el-time-select>
              </el-form-item>

              <el-form-item label="Notes" :label-width="formLabelWidth" style="margin-top: 20px">
                <el-input
                    type="textarea"
                    :rows="3"
                    placeholder="Additional notes for the repairman"
                    v-model="feedback">
                </el-input>
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
      roomData: [], // Store room information
      workFile: null,
      fileList: [],
      dialogFormVisible: false,
      feedback: '',
      form: {
        managerID: null,
        orderID: null,
      },
      formLabelWidth: '120px',
      startTime: '',
      endTime: '',
      dateValue: '',
      currentRow: null,
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() < (Date.now() - 3600 * 1000 * 24)
        },
        shortcuts: [{
          text: 'Today',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: 'Tomorrow',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }]
      },
    }
  },

  created() {
    this.loadRoomData();
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
    formatDateTime(dateString) {
      if (!dateString || dateString.includes('2000-01-01')) return 'N/A';
      const date = new Date(dateString);
      return date.toLocaleString();
    },

    // Load room data
    loadRoomData() {
      this.$axios({
        method: 'get',
        url: '/room/getRoomsInfo'
      })
      .then((res) => {
        if (res.data && res.data.data) {
          this.roomData = res.data.data;
        } else {
          console.log("Failed to load room data");
          this.roomData = []; // Initialize as empty array if failed
        }
      })
      .catch((err) => {
        console.log("Error loading room data:", err);
        this.roomData = []; // Initialize as empty array if failed
      });
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

    // Load orders based on route type
    loadOrders() {
        this.isLoading = true;
        const formData = new FormData();
        formData.append("token", this.$store.state.token);
        formData.append("type", this.$route.query.type || '0');
        formData.append("isUser", this.$store.state.userState);
        
        // Always use getAllOrders endpoint for all user types
        const url = '/service/getAllOrders';
        
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
            
            // If user is a manager (userType === 2), filter to only show their assigned orders
            if (this.$store.state.userType === 2) {
                const managerID = this.$store.state.userID;
                if (managerID) {
                filteredOrders = filteredOrders.filter(order => order.managerID === managerID);
                }
            }
            
            // Process data to include additional room and repairman information
            this.tableData = this.processOrderData(filteredOrders);
            } else {
            console.log("API Error:", res.data);
            this.$message.error("Failed to load orders: " + (res.data.errmsg || "Unknown error"));
            this.tableData = [];
            }
            this.isLoading = false;
        })
        .catch((err) => {
            console.log("API Error:", err);
            this.$message.error("Failed to load orders. Please try again later.");
            this.tableData = [];
            this.isLoading = false;
        });
        },

    // Process order data to include room and repairman information
    processOrderData(orders) {
      return orders.map(order => {
        let repairmanName = 'Not assigned';
        let repairmanEmail = 'N/A';
        let roomNumber = `Room ${order.roomID}`;
        
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
        
        // Get room number for this order
        if (this.roomData && this.roomData.length > 0) {
          const room = this.roomData.find(r => r.roomID === order.roomID);
          if (room) {
            roomNumber = room.roomNumber;
          }
        }
        
        return {
          ...order,
          roomNumber: roomNumber,
          repairmanName: repairmanName,
          repairmanEmail: repairmanEmail
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
    
    onChangeUpload(file) {
      this.workFile = file;
    },
    
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },

    // Assign repairman to the order
    assignRepairman() {
      if (!this.form.managerID) {
        this.$message.warning("Please select a repairman");
        return;
      }
      
      if (!this.dateValue || !this.startTime || !this.endTime) {
        this.$message.warning("Please select date and time");
        return;
      }

      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.form.orderID);
      formData.append("managerID", this.form.managerID);
      formData.append("feedback", this.feedback);
      formData.append("startTime", this.dateValue + " " + this.startTime);
      formData.append("endTime", this.dateValue + " " + this.endTime);
      
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
    // Corrected submitSolution method with proper parameter names
    submitSolution() {
    if (!this.solveMethod) {
        this.$message.warning("Please enter solution details");
        return;
    }
    
    const formData = new FormData();
    formData.append("token", this.$store.state.token);
    formData.append("orderID", this.fixID);
    formData.append("method", this.solveMethod); // Changed from "solution" to "method"
    
    console.log("Submitting with orderID:", this.fixID);
    
    this.$axios({
        method: 'post',
        url: '/service/finishOrder',
        data: formData
    })
    .then((res) => {
        console.log("API response:", res.data);
        if (res.data.errno === 0) {
        this.dialogFormVis2 = false;
        this.$message.success("Order completed successfully");
        
        // Add to knowledge base
        this.addToKnowledgeBase();
        
        // Reload orders
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

    // Add to knowledge base method
    addToKnowledgeBase() {
    // Find the current order to get the problem description
    const currentOrder = this.tableData.find(order => order.orderID === this.fixID);
    
    if (!currentOrder) {
        console.warn("Could not find order details for knowledge base entry");
        return;
    }
    
    const problemDescription = currentOrder.description || "";
    
    const knowledgeData = new FormData();
    knowledgeData.append("token", this.$store.state.token);
    knowledgeData.append("problem", problemDescription);
    knowledgeData.append("solution", this.solveMethod);
    
    this.$axios({
        method: 'post',
        url: '/manager/addKnowledge',
        data: knowledgeData
    })
    .then((res) => {
        console.log("Knowledge base API response:", res.data);
        
        if (res.data.errno === 0) {
        this.$message.success("Solution added to knowledge base");
        } else {
        console.warn("Knowledge base API returned error:", res.data);
        this.$message.warning("Order completed but could not add to knowledge base");
        }
    })
    .catch((err) => {
        console.error("Error adding to knowledge base:", err);
        this.$message.warning("Order completed but could not add to knowledge base");
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
</style>

<style>
.el-table .warning-row {
  background: rgba(245,108,108, 0.12);
}

.el-table .stripe-row {
  background: rgb(250,250,250);
}
</style>

<style>
.operations-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.status-with-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.el-tag {
  margin-right: 0;
}
</style>