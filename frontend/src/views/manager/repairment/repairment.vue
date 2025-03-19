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
          <el-table-column
              label="编号" align="center"
              width="50">
            <template slot-scope="scope">
              <span>{{ scope.$index + pageSize * (currentPage - 1) + 1 }}</span>
            </template>
          </el-table-column>
          <el-table-column
              prop="submitTime"
              label="报修时间"
              width="150"
              sortable>
          </el-table-column>
          <el-table-column
              prop="roomNumber"
              label="房间号"
              width="100"
              align="center"
          >
          </el-table-column>
          <el-table-column
              prop="companyName"
              label="公司"
              min-width="8"
              align="center"
          >
          </el-table-column>
          <el-table-column
              prop="contactName"
              label="报修人姓名"
              width="120"
              align="center"
          >
          </el-table-column>
          <el-table-column
              prop="contactPhone"
              label="联系方式"
              width="140"
              align="center"
          >
          </el-table-column>
          <el-table-column
              prop="description"
              label="问题描述"
              min-width="8"
              align="center"
          >
          </el-table-column>
          <el-table-column
              label="操作"
              width="180"
              align="center"
          >
            <template v-slot="scope">
              <div v-if="$route.query.type==='1'&& scope.row.status===2 && $store.state.userType===1">
<!--                <el-button type="success" size="medium" plain>已处理</el-button>-->
                <el-popconfirm
                    confirm-button-text='添加'
                    cancel-button-text='不添加'
                    confirm-button-type="success"
                    cancel-button-type="warning"
                    title="是否将该工单添加到知识库"
                    @confirm="addForm(scope.row.orderID)"
                    @cancel="deleteForm(scope.row.orderID)"
                >
                  <el-button type="primary" size="medium" plain slot="reference">添加到知识库</el-button>
                </el-popconfirm>
              </div>
              <div v-else-if="$route.query.type==='1'&& scope.row.status===2">
                <el-button type="success" size="medium" plain>已处理</el-button>
              </div>
              <div v-else-if="$route.query.type==='1'&& scope.row.status===1">
                <el-button type="warning" size="medium" plain>待维修</el-button>
              </div>
              <div v-else-if="$route.query.type==='1'&& scope.row.status===3">
                <el-button type="warning" size="medium" plain>已打回</el-button>
              </div>
              <div v-else-if="$route.query.type==='1'&& scope.row.status===4">
                <el-button type="success" size="medium" plain>已处理</el-button>
              </div>
              <div v-else-if="$store.state.userType===1">
                <el-button type="danger" size="medium" plain @click=openDialog(scope.row.orderID,scope.row.description)>派发</el-button>
              </div>
              <div v-else>
                <el-button type="danger" size="small" plain @click=openWorkerDialog(scope.row.orderID)>处理</el-button>
                <el-button type="primary" size="small" plain @click=downloadPDF(scope.row.orderID)>下载维修单</el-button>
              </div>
            </template>
          </el-table-column>
          <div v-if="t==='1'">
            <el-table-column
                prop="solvePerson"
                label="维修人员人姓名"
                width="120"
                align="center"
            >
            </el-table-column>
            <el-table-column
                prop="managePhoneNumber"
                label="联系方式"
                width="140"
                align="center"
            >
            </el-table-column>
          </div>
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

        <div>
          <el-dialog title="维修报告" :visible.sync="dialogFormVis2">
            <el-input
                type="textarea"
                :rows="5"
                placeholder="请输入内容"
                v-model="solveMethod">
            </el-input>
            <div style="margin-top: 30px">
              <el-upload
                  class="upload-demo"
                  ref="upload"
                  :on-remove="handleRemove"
                  :on-change="onChangeUpload"
                  :file-list="fileList"
                  :limit="1"
                  :auto-upload="false">
                <el-button slot="trigger" size="small" type="primary">上传维修单图片</el-button>
              </el-upload>
            </div>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVis2 = false">取 消</el-button>
              <el-button type="primary" @click=submitSolution>确 定</el-button>
            </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog title="指派维修人员" :visible.sync="dialogFormVisible" width="65%" top="2%">
            <el-form :model="form">
              <el-form-item label="问题描述" :label-width="formLabelWidth">
                <div>{{this.tempDescription}}</div>
              </el-form-item>
              <el-collapse v-model="activeNames" accordion @change="handleChange">
              <el-form-item label="推荐维修工" :label-width="formLabelWidth">
                <el-collapse-item name="1">
                <el-table
                    ref="singleTable2"
                    :data="recommendData"
                    highlight-current-row
                    @current-change="handleRecommendRowChange"
                  >
                  <el-table-column
                      type="index"
                      min-width="2">
                  </el-table-column>
                  <el-table-column
                      property="trueName"
                      label="维修人员姓名"
                      min-width="4">
                  </el-table-column>
                  <el-table-column
                      property="type"
                      label="种类"
                      min-width="4">
                    <template v-slot="scope">
                      <div v-if="scope.row.type===2">水工</div>
                      <div v-else-if="scope.row.type===3">电工</div>
                      <div v-else>机械工</div>
                    </template>
                  </el-table-column>
                  <el-table-column
                      property="startTime"
                      label="开始时间"
                      width="280">
                  </el-table-column>
                  <el-table-column
                      property="endTime"
                      label="结束时间"
                      width="280">
                  </el-table-column>
                  <el-table-column
                      property="taskNum"
                      label="当前工作数量"
                      min-width="4">
                  </el-table-column>
                </el-table>
                </el-collapse-item>
              </el-form-item>

              <el-form-item label="选择维修工" :label-width="formLabelWidth">

                  <el-collapse-item  name="2">
                <span>
                  <el-date-picker
                      v-model="dateValue"
                      value-format="yyyy-MM-dd"
                      align="right"
                      type="date"
                      placeholder="选择日期"
                      :picker-options="pickerOptions">
                  </el-date-picker>
                </span>
                <el-time-select
                    style="margin-left: 20px"
                    placeholder="起始时间"
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
                    placeholder="结束时间"
                    value-format="HH:mm:ss"
                    v-model="endTime"
                    :picker-options="{
                    start: '08:30',
                    step: '00:15',
                    end: '18:30',
                  minTime: startTime
                 }">
                </el-time-select>
                <span><el-button style="margin-left: 30px" @click="getWorkerList">查询</el-button></span>

                <div>
                  <el-table
                      ref="singleTable1"
                      :data="workerData"
                      highlight-current-row
                      @current-change="handleRowChange"
                      style="width: 80%;">
                    <el-table-column
                        type="index"
                        min-width="2">
                    </el-table-column>
                    <el-table-column
                        property="trueName"
                        label="维修人员姓名"
                        min-width="4">
                    </el-table-column>
                    <el-table-column
                        property="type"
                        label="种类"
                        min-width="4">
                      <template v-slot="scope">
                        <div v-if="scope.row.type===2">水工</div>
                        <div v-else-if="scope.row.type===3">电工</div>
                        <div v-else>机械工</div>
                      </template>
                    </el-table-column>
                    <el-table-column
                        property="taskNum"
                        label="当前工作数量"
                        width="200"
                        sortable>
                    </el-table-column>
                  </el-table>
                </div>
                  </el-collapse-item>
              </el-form-item>
              </el-collapse>

              <el-form-item label="填写反馈意见" :label-width="formLabelWidth" style="margin-top: 30px">
                <el-input
                    type="textarea"
                    :rows="5"
                    placeholder="请输入内容"
                    v-model="feedback">
                </el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
              <el-button type="warning" @click=returnForm>打 回</el-button>
              <el-button type="primary" @click=this.chooseWorker>确 定</el-button>
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
      tempDescription:'',
      isLoading:true,
      t:'0',
      solveMethod: null,
      dialogFormVis2: false,
      fixID: null,
      currentPage: 1,
      pageSize: 10,
      workerData: [],
      tableData: [],
      firstData: [],
      finishedData: [],
      recommendData:[],
      activeNames: '1',
      workFile:null,
      fileList:[],
      startRecommendTime:null,
      endRecommendTime:null,
      dialogFormVisible: false,
      feedback: '',
      form: {
        managerID: null,
        solveTime: null,
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
    }
  },

  created() {
    this.t=this.$route.query.type;
    // this.createView(0);
    this.createView(this.t);
  },


  watch: {
    '$route.query.type': {
      handler(newVal, oldVal) {
        // this.t=this.$route.query.type;
        // if (this.$route.query.type === '0') this.tableData = this.firstData;
        // else this.tableData = this.finishedData;
        this.tableData=[];
        this.isLoading=true;
        this.createView(this.$route.query.type)
      },
      deep: true
    }
  },

  methods: {
    setCurrent(row) {
      this.$refs.singleTable1.setCurrentRow(row);
      this.$refs.singleTable2.setCurrentRow(row);
    },
    handleSizeChange(val) {
      this.pageSize = val;
      console.log(this.pageSize);
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      console.log(this.currentPage);
    },
    handleRecommendRowChange(val) {
      this.currentRow = val;
      this.form.managerID = val.managerID;
      this.startRecommendTime=val.startTime;
      this.endRecommendTime=val.endTime;
    },
    handleRowChange(val) {
      this.currentRow = val;
      this.form.managerID = val.managerID;
    },
    handleChange() {
      this.currentRow = null;
      this.form.managerID = null;
      this.startRecommendTime=null;
      this.endRecommendTime=null;
      this.setCurrent();
    },
    openDialog(ID,des) {
      this.dialogFormVisible = true;
      this.form.orderID = ID;
      this.tempDescription=des;
      this.getRecommendWorker()
    },
    openWorkerDialog(ID) {
      this.dialogFormVis2 = true;
      this.fixID = ID;
    },
    onChangeUpload(file) {
      this.workFile=file;
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    deleteForm(ID){
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", ID);
      formData.append("operation", 0);
      this.$axios({
        method: 'post',
        url: '/serviceman/orderKnowledge',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.$message.warning("未添加到知识库");
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
    addForm(ID){
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", ID);
      formData.append("operation", 1);
      this.$axios({
        method: 'post',
        url: '/serviceman/orderKnowledge',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.$message.success("已添加到知识库");
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
    returnForm(){
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.form.orderID);
      formData.append("feedback", this.feedback);
      this.$axios({
        method: 'post',
        url: '/serviceman/rejectOrder',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.dialogFormVis2 = false;
              this.$message.success("工单已打回");
              this.$router.go(0);
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    },
    downloadPDF(ID){
      const formData = new FormData();
      formData.append("orderID", ID);
      this.$axios({
        method: 'post',
        url: '/serviceman/getFormUrl',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              // window.alert(JSON.stringify(res.data))
              window.open(res.data.url)
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    },
    getRecommendWorker(){
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.form.orderID);
      this.$axios({
        method: 'post',
        url: '/serviceman/IntelligenceOrder',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              // window.alert(JSON.stringify(res.data))
              this.recommendData = res.data.managers;
              for(var i=0;i<this.recommendData.length;i++){
                var arr=new Array(5);
                arr=this.recommendData[i].startTime.split('T');
                this.recommendData[i].startTime=arr[0]+" "+arr[1];
                arr=this.recommendData[i].endTime.split('T');
                this.recommendData[i].endTime=arr[0]+" "+arr[1];
              }
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    },
    getWorkerList() {
      if (this.dateValue.length === 0 || this.startTime.length === 0 || this.endTime.length === 0) {
        this.$message.warning("请选择时间和日期");
        return;
      }
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("startTime", this.dateValue + " " + this.startTime);
      formData.append("endTime", this.dateValue + " " + this.endTime);
      this.$axios({
        method: 'post',
        url: '/serviceman/checkManager',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              // window.alert(JSON.stringify(res.data))
              this.workerData = res.data.managers;
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    },
    chooseWorker() {
      if(this.form.managerID===null){
        this.$message.warning("请选择维修工");
      }
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.form.orderID);
      formData.append("managerID", this.form.managerID);
      formData.append("feedback", this.feedback);
      if(this.startRecommendTime===null){
        formData.append("startTime", this.dateValue + " " + this.startTime);
      }
      else{
        formData.append("startTime",this.startRecommendTime);
      }

      if(this.endRecommendTime===null){
        formData.append("endTime", this.dateValue + " " + this.endTime);
      }
      else{
        formData.append("endTime",this.endRecommendTime);
      }
      this.$axios({
        method: 'post',
        url: '/serviceman/appointOrder',
        data: formData
      })
          .then((res) => {
            this.dialogFormVisible = false;
            if (res.data.errno === 0) {
              console.log(res.data);
              this.$message.success("提交成功");
              this.$router.go(0);
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    },
    submitSolution() {
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("orderID", this.fixID);
      formData.append("solution", this.solveMethod);
      formData.append("image",this.workFile.raw);
      this.$axios({
        method: 'post',
        url: '/serviceman/finishOrder',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.dialogFormVis2 = false;
              this.$message.success("提交成功");
              this.$router.go(0);
            } else {
              console.log(res.data);
            }
          })
          .catch((err) => {
            console.log(err);
          });
    },
    setTimeOut({row, rowIndex}) {
      // rowIndex是行数, 从0开始
      var nowTime=Date.parse(new Date());
      var submitTime=Date.parse(new Date(row.submitTime));
      var dealTime=Math.abs(parseInt((nowTime - submitTime) / 1000 / 3600));
      if(dealTime>0 && this.$route.query.type==='0' && this.$store.state.userType === 1) {
        return 'warning-row'
      }
      if(rowIndex % 2 !== 0) {
        return 'strike-row';
      }
      return '';
    },
    createView(type) {
      const formData = new FormData()
      formData.append("token", this.$store.state.token);
      formData.append("type", type);
      formData.append("isUser", this.$store.state.userState);
      this.$axios({
        method: 'post',
        url: '/service/getAllOrders',
        data: formData
      })
          .then((res) => {
            if (res.data.errno === 0) {
              this.tableData=res.data.data;
              this.isLoading=false;
              // window.alert(JSON.stringify(res.data))
              // if (type === 0) {
              //   this.firstData = res.data.data;
              // } else {
              //   this.finishedData = res.data.data;
              // }
              //
              // if(this.$route.query.type==='0'){
              //   this.tableData = this.firstData;
              // }
              // else{
              //   this.tableData = this.finishedData;
              // }

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

.el-table .strike-row {
    background: rgb(250,250,250);
}
</style>
