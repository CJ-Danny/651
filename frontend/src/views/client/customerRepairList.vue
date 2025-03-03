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
      <el-button type="primary" plain @click="dialogFormVisible = true;">Submit new repair orders</el-button>
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
            width="150">
        </el-table-column>
        <el-table-column
            prop="roomNumber"
            label="Room"
            min-width="5"
            align="center"
        >
        </el-table-column>
        <el-table-column
            prop="status"
            label="Status"
            width="100"
            align="center"
        >
          <template v-slot="scope">
            <div v-if="scope.row.status===0"><el-button type="info" plain size="small"> 未处理</el-button></div>
            <div v-if="scope.row.status===1"><el-button type="warning" plain size="small"> 待维修</el-button></div>
            <div v-if="scope.row.status===2||scope.row.status===4"><el-button type="success" plain size="small" @click="openDetail(scope.row)"> 已完成—详情</el-button></div>
            <div v-if="scope.row.status===3"><el-button type="danger" plain size="small"> 时间不可用</el-button></div>
          </template>
        </el-table-column>
        <el-table-column
            prop="solvePerson"
            label="Maintenance Worker"
            min-width="10"
            align="center"
        >
        </el-table-column>
        <el-table-column
            prop="startTime"
            label="Estimated Repair Time"
            width="300"
            align="center"
        >
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
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '明天',
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
          { required: true, message: '请选择需要维修的房间号', trigger: 'blur' }
        ],
        startDate: [
          { type: 'date', required: true, message: '请选择日期', trigger: 'blur' }
        ],
        date2: [
          { type: 'date', required: true, message: '请选择日期', trigger: 'blur' }
        ],
        description: [
          { required: true, message: '请描述您的问题', trigger: 'blur' }
        ],
      },
      rules2: {
        startDate: [
          { type: 'date', required: true, message: '请选择日期', trigger: 'blur' }
        ],
        date2: [
          { type: 'date', required: true, message: '请选择日期', trigger: 'blur' }
        ],
      }
    }
  },

  created() {
    const formData = new FormData()
    formData.append("token", this.$store.state.token);
    this.$axios({
      method: 'post',
      url: '/serviceman/checkUserOrder',
      data: formData
    })
        .then((res) => {
          if (res.data.errno === 0) {
            // window.alert(JSON.stringify(res.data))
            this.tableData=res.data.data;
            this.form.contactPerson=res.data.trueName;
            this.form.contactNumber=res.data.phoneNumber;
            for(var i=0;i<this.tableData.length;i++){
              if(this.tableData[i].status===0) {
                this.tableData[i].solvePerson="-";
                this.tableData[i].startTime="-";
                this.tableData[i].feedback="-";
                this.tableData[i].managePhoneNumber="-";
              }

              if(this.tableData[i].status===0||this.tableData[i].status===1){
                this.tableData[i].solution="-";
              }

              if(this.tableData[i].status===3){
                this.tableData[i].solvePerson="-";
                this.tableData[i].startTime="-";
                this.tableData[i].managePhoneNumber="-";
                this.tableData[i].solution="-";
              }
            }
          } else {
            console.log(res.data);
          }
        })
        .catch((err) => {
          console.log(err);
        });


    this.$axios({
      method: 'post',
      url: '/roommanage/getUserRooms',
      data: formData
    })
        .then((res) => {
          if (res.data.errno === 0) {
            this.roomOptions=res.data.data;
          } else {
            console.log(res.data);
          }
        })
        .catch((err) => {
          console.log(err);
        });
  },

  methods: {
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
      formData.append("roomID",this.form.roomID);
      formData.append("description",this.form.description);
      formData.append("contactName",this.form.contactPerson);
      formData.append("contactPhone",this.form.contactNumber);
      formData.append("startTime1",this.form.startDate+" "+this.form.startTime);
      formData.append("startTime2",this.form.date2+" "+this.form.time2);
      this.$axios({
        method: 'post',
        url: '/serviceman/createOrder',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.$message.success("报修成功");
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
    },
    resubmitOrder(){
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID",this.tempOrder.orderID)
      formData.append("startTime1",this.returnForm.startDate+" "+this.returnForm.startTime);
      formData.append("startTime2",this.returnForm.date2+" "+this.returnForm.time2);
      this.$axios({
        method: 'post',
        url: '/serviceman/reSubmitOrder',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.$message.success("重新提交成功");
              this.returnDialogVis = false;
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
