<template>
  <div style="margin-left: 6vw;margin-top:30px">
    <div style="display: flex">
      <div style="background-color: #FBFBFB; width: 50vw; height: 50px; display: flex; align-items: center; white-space: nowrap; overflow: hidden;">
        <div style="background-color: #0d9fda;width:10px;height:50px"></div>
        <div style="padding-left: 25px">You can check the status of your submitted repair orders here, or submit new repair orders.</div>
      </div>
    </div>
    <div style="float:right;margin-right: 50px;margin-top: -70px"><img src="../../assets/repair/logo.png"></div>

    <div style="float:right;margin: 40px -8vw 20px 0">

    <el-button type="primary" plain @click="openRepairDialog">Submit new repair orders</el-button>
  </div>

    <div>
      <el-dialog title="Submit new repair orders" :visible.sync="dialogFormVisible">
        <el-form :model="form" :rules="rules">
          <el-form-item label="roomNumber" :label-width="formLabelWidth" prop="roomNumber">
            <el-select v-model="form.roomID" placeholder="Please Select">
              <el-option
                  v-for="item in roomOptions"
                  :key="item.roomId"
                  :label="item.roomNumber"
                  :value="item.roomId">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Description" :label-width="formLabelWidth" prop="description">
            <el-input type="textarea" v-model="form.description" :rows="5" placeholder="Describe the problem"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancel</el-button>
          <el-button type="primary" @click="createOrder">Confirm</el-button>
        </div>
      </el-dialog>
    </div>

     <div>
      <el-dialog title="Re-fill the repair order" :visible.sync="returnDialogVis">
        <el-form :model="returnForm" :rules="rules2">
          <el-form-item label="roomNumber" :label-width="formLabelWidth" prop="roomNumber">
            <div>{{this.tempOrder.roomNumber}}</div>
          </el-form-item>
          <el-form-item label="Description" :label-width="formLabelWidth" prop="description">
            <div>{{this.tempOrder.description}}</div>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="returnDialogVis = false">Cancel</el-button>
          <el-button type="primary" @click="resubmitOrder">Resubmit</el-button>
        </div>
      </el-dialog>
    </div>

    <div>
      <el-dialog title="View repair details" :visible.sync="detailDialog" top="2%">
        <el-form>
          <el-form-item label="roomNumber" :label-width="formLabelWidth">
            <div>{{this.tempOrder.roomNumber}}</div>
          </el-form-item>
          <el-form-item label="repairman's name" :label-width="formLabelWidth">
            <div>{{this.tempOrder.solvePerson}}</div>
          </el-form-item>
          <el-form-item label="repair time" :label-width="formLabelWidth">
            <div>{{this.tempOrder.solveTime}}</div>
          </el-form-item>
          <el-form-item label="solution" :label-width="formLabelWidth">
            <div>{{this.tempOrder.solution}}</div>
          </el-form-item>
          <el-form-item label="Repair Order" :label-width="formLabelWidth">
            <div><img :src="this.tempOrder.pic" style="width: 90%"></div>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="detailDialog = false">Close</el-button>
        </div>
      </el-dialog>
    </div>

    <div>
      <el-table
      :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
      stripe
      style="width: 95%"
      empty-text="No rental history available">
      <el-table-column
          label="No." align="center"
          width="100">
        <template slot-scope="scope">
          <span>{{ scope.$index + pageSize * (currentPage- 1) + 1 }}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="submitTime"
        label="Submission Time"
        sortable
        width="180"
        :formatter="formatDateTime">
      </el-table-column>

      <el-table-column
        prop="assignTime"
        label="Assigned Time"
        sortable
        width="180"
        :formatter="formatDateTime">
      </el-table-column>

      <el-table-column
        prop="finishTime"
        label="Completion Time"
        sortable
        width="180"
        :formatter="formatDateTime">
      </el-table-column>
      <el-table-column
          prop="roomNumber"
          label="Room"
          min-width="20"
          align="center">
      </el-table-column>
      <el-table-column
        prop="description"
        label="Problem Description"
        min-width="50"
        show-overflow-tooltip>
      </el-table-column>
      <el-table-column
          prop="status"
          label="Status"
          width="200"
          align="center">
        <template v-slot="scope">
          <div v-if="scope.row.status===0"><el-button type="info" plain size="small"> Unprocessed</el-button></div>
          <div v-if="scope.row.status===1"><el-button type="warning" plain size="small"> Waiting</el-button></div>
          <div v-if="scope.row.status===2||scope.row.status===4"><el-button type="success" plain size="small" @click="openDetail(scope.row)"> Complete</el-button></div>
          <div v-if="scope.row.status===3"><el-button type="danger" plain size="small"> Time unavailable</el-button></div>
        </template>
      </el-table-column>
    </el-table>
    </div>
  </div>
</template>

<script>
export default {
  name: "customerRepairList",

  data(){
    return{
      returnDialogVis:false,
      detailDialog:false,
      orderID:null,
      tempOrder:[],
      currentPage:1,
      pageSize:10,
      roomOptions:[

      ],
      tableData:[

      ],
      dialogFormVisible: false,
      form: {
        roomID:'',
        description:'',
        contactPerson:'',
        contactNumber:'',
        startDate:'',
        startTime:'',
        date2:'',
        time2:'',
      },
      returnForm:{
        startDate:'',
        startTime:'',
        date2:'',
        time2:'',
      },
      formLabelWidth: '130px',
      pickerOptions: {
        shortcuts: [{
          text: 'today',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: 'tomorrow',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }
        ],
      },
      rules: {
        roomNumber: [
          { required: true, message: 'Please Select room number', trigger: 'blur' }
        ],
        startDate: [
          { type: 'date', required: true, message: 'Please Select date', trigger: 'blur' }
        ],
        date2: [
          { type: 'date', required: true, message: 'Please Select date', trigger: 'blur' }
        ],
        description: [
          { required: true, message: 'Describe your problem', trigger: 'blur' }
        ],
      },
      rules2: {
        startDate: [
          { type: 'date', required: true, message: 'Please Select date', trigger: 'blur' }
        ],
        date2: [
          { type: 'date', required: true, message: 'Please Select date', trigger: 'blur' }
        ],
      }
    }
  },

  created() {
    const formData = new FormData()
    formData.append("token", this.$store.state.token);
    this.$axios({
      method: 'post',
      url: 'user/getOrders',
      data: formData
    })
    .then((res) => {
          if (res.data.errno === 0) {
            this.tableData = res.data.data.map(item => ({
              ...item,
              roomNumber: `Room ${item.roomNumber}`, 
              
              solvePerson: "-", 
              startTime: "-"  
            }));
          } else {
            console.log(res.data);
          }
        })
        .catch((err) => {
          console.log(err);
        });



   
  },

  methods: {
    formatDateTime(row, column, cellValue) {
      // Check if the cellValue is null or has the default timestamp value
      if (!cellValue || cellValue === "2000-01-01T00:00:00Z" || cellValue === "1999-12-31 19:00:00" || cellValue === "1999-12-31T19:00:00Z") {
        return "—";
      }
      
      // Otherwise format the date normally
      const date = new Date(cellValue);
      return date.toLocaleString('zh-CN', { 
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false 
      }).replace(/\//g, '-');
    },
    openRepairDialog() {
      this.dialogFormVisible = true;
      this.fetchRoomOptions(); 
    },
    
    fetchRoomOptions() {
      const formData = new FormData();
      formData.append("token", this.$store.state.token);
      
      this.$axios({
        method: 'post',
        url: 'user/getHomeInfo',
        data: formData
      })
      .then((res) => {
        if (res.data.errno === 0) {
          this.roomOptions = res.data.data.rentList; 
          console.log("Successful:", this.roomOptions);
        } else {
          this.$message.error("Failed to load room data");
        }
      })
      .catch((err) => {
        console.log("Fail:", err);
        this.$message.error("Network error");
      });
    },
    handleSizeChange(val) {
      this.pageSize = val;
      console.log(this.pageSize);
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      console.log(this.currentPage);
    },
    submitReturn(order){
      this.returnDialogVis=true;
      this.tempOrder=order;
    },
    openDetail(order){
      this.detailDialog=true;
      this.tempOrder=order;
    },
    createOrder(){
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("roomId",this.form.roomID);
      formData.append("description",this.form.description);
      formData.append("contactName",this.form.contactPerson);
      formData.append("contactPhone",this.form.contactNumber);
      formData.append("startTime1",this.form.startDate+" "+this.form.startTime);
      formData.append("startTime2",this.form.date2+" "+this.form.time2);
      this.$axios({
        method: 'post',
        url: '/user/applyOrder',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.$message.success("Repair successfully reported");
              this.dialogFormVisible = false;
              setTimeout(() => {
                this.$router.go(0);
              }, 500);
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    }
  }
}
</script>

<style scoped>
.pageDiv{
  padding-top: 30px;
  text-align:center;
  padding-bottom: 50px;
}
</style>