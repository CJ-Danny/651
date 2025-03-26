<template>
  <div style="background-color: rgb(250,252,255);overflow-x: hidden">
    <el-row>
      <el-col :span="18" style="margin-left: 2%;margin-top: 1%">
        <div style="color: rgb(32, 33, 36);font-family: zeitung, sans-serif;
    margin-bottom: 16px;font-size: 30px;margin-left: 50px;
    line-height: 44px;
    font-weight: 700;">
          Serviceman List
          <br/>
          
          <div style="display: flex;align-items: start">
             <span style="color: black;font-size: 15px;line-height: 24px;margin-top: 30px; font-weight: 400;">
          <span style="color: red">&nbsp;{{count || 0}}&nbsp;</span> Serviceman in total.
              </span>
           <!-- <img src="../../../assets/peopleManagement/时间管理04.png" style="height: 15vh;">
           -->
          </div>
         
        </div>
        
        <div style="display: flex;align-items: center">
          <el-button type="primary" class="newButton" @click="dialogFormVisible = true" style="margin-left: 50px">New</el-button>
          <el-button type="primary" class="newButton" @click="openDeleteDialog" style="margin-left: 50px">Delete</el-button>
        </div>
        <br/>
      </el-col>
    </el-row>
     
        <el-dialog title="Create New Service Man" :visible.sync="dialogFormVisible" >
        <el-form :model="form" :rules="formRules" ref="formRef">
          <el-form-item prop="name" label="Name" :label-width="formLabelWidth">
            <el-input v-model="form.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="password" label="Password" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="email" label="Email" :label-width="formLabelWidth">
            <el-input v-model="form.email" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="type" label="Type" :label-width="formLabelWidth">
            <el-select v-model="form.type" placeholder="Please select a type">
              <el-option label="Water" value=1></el-option>
              <el-option label="Electricity" value=2></el-option>
              <el-option label="Mechanic" value=3></el-option>
            </el-select>
          </el-form-item>
          <el-form-item prop="status" label="Status" :label-width="formLabelWidth">
            <el-select v-model="form.status" placeholder="Please select a status">
              <el-option label="Busy" value=0></el-option>
              <el-option label="Available" value=1></el-option>
            </el-select>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancle</el-button>
          <el-button type="primary" @click="handleCreate">Ok</el-button>
        </div>
      </el-dialog>

      <el-dialog :visible.sync="deleteDialogVisible" title="Delete Serviceman">
        <el-table :data="allData" style="width: 100%">
          <el-table-column label="ID" prop="userID" width="100" />
          <el-table-column label="Name" prop="name" />
          <el-table-column label="Operation" width="120">
            <template slot-scope="scope">
              <el-button type="danger" size="mini" @click="confirmDelete(scope.row)">Delete</el-button>
            </template>
          </el-table-column>
        </el-table>

        <span slot="footer">
          <el-button @click="deleteDialogVisible = false">Close</el-button>
        </span>
      </el-dialog>

      <el-dialog
        title="Confirm Deletion":visible.sync="deleteConfirmVisible" width="30%">
        <p>Are you sure you want to delete serviceman <strong>{{ deleteTarget?.name }}</strong>?</p>
        <span slot="footer">
          <el-button @click="deleteConfirmVisible = false">Cancel</el-button>
          <el-button type="primary" @click="handleDelete">Confirm</el-button>
        </span>
      </el-dialog>

    <div class="formBackground" style="width: 85vw;background-color: white;height: 65vh;margin-left: 5vw;

border-top-left-radius: 20px;border-top-right-radius: 20px;display: flex;flex-direction: column;align-items: center">
      <div style="height: 20px"></div>
      <el-table
          :data="tableData.slice((table_page - 1) * 7, table_page * 7)"
          style="width: 78vw;margin-left: 2.5vw;margin-top: 2vh">
        <el-table-column
            label="Id"
            width="50"
            prop="managerId">
        </el-table-column>
        <el-table-column
            label="Name"
            prop="name"
            width="100">

        </el-table-column>
        <el-table-column
            label="Email"
            prop="email"
            width="300">

        </el-table-column>
        <el-table-column
            prop="type"
            label="maintaince type"
            width="100"
           >
          <template slot-scope="scope">
            <el-tag v-if="scope.row.type===2" type="primary" disable-transitions>Water </el-tag>
            <el-tag v-if="scope.row.type===3" type="warning" disable-transitions>Electricity </el-tag>
            <el-tag v-if="scope.row.type===4" type="info" disable-transitions>Mechanic </el-tag>

          </template>
        </el-table-column>
        <el-table-column
            prop="status"
            label="Status"
            width="100"
            >
          <template slot-scope="scope">
            <el-tag
                :type="scope.row.status ? 'success' : 'danger'"
                disable-transitions><div v-if="scope.row.status" >Avalible</div>
              <div v-if="!scope.row.status">Unavailable</div>
            </el-tag>
          </template>
        </el-table-column>
        
        <el-table-column
            label="Finished Orders"
            prop="finished_num"
            width="150">
        </el-table-column>

        <el-table-column
            label="Unfinished Orders"
            prop="unfinished_num"
            width="150">

        </el-table-column>

      </el-table>
        <el-pagination
            layout="prev, pager, next"
            :total="tableData.length"
            :current-page.sync="table_page"
            :page-size="8"
        >
        </el-pagination>
      <br/>
    </div>
    <div style="height: 1vh"></div>

  </div>
</template>

<script>
export default {
  name: "maintainerInfo",
  data(){
    return{
      count:'',
      allData:[],
      editVisible:false,
      checkVisible:false,
      table_page:1,
      dialogFormVisible:false,
      formLabelWidth: '120px',
      tableData: [
      ],
      form:{
        name: '',
        password: '',
        email: '',
        type:'',
        status:''
      },
      formRules:{
        name:[
          {required:true, message: 'Please enter username', trigger: 'blur'}
        ],
        password:[
          { required:true, message: 'Pleaes enter password', trigger: 'blur' },
          { min: 2, max: 10, message: 'Password length needs to be [2,10]', trigger: 'blur' }
        ],
        email:[
          { required:true, message: 'Please enter email', trigger: 'blur' },
        ],
        type:[
          {required:true, message: 'Please select type', trigger: 'change' }
        ],
        status: [
          { required: true, message: 'Please select status', trigger: 'change' }
        ]
      },
      deleteDialogVisible: false,
      deleteConfirmVisible: false,
      deleteTarget: null, 
    }
  },
  created() {
    this.getAllFixer()
  },
  watch:{
  },
  methods:{
    getAllFixer(){
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      this.$axios({
        method: 'post',
        url: '/manager/getManagerInfo',
        data: formData,
      })
          .then((res) => {
            this.tableData=res.data.data
            this.count=this.tableData.length
            this.allData=res.data.data
          })
          .catch((err) => {
            console.log(err);
          });
    },
    handleCreate(){
      this.$refs.formRef.validate((valid) =>{
        if(valid){
          this.dialogFormVisible=false
          const formData = new FormData();
          formData.append('name', this.form.name);
          formData.append('password', this.form.password);
          formData.append('email', this.form.email);
          formData.append('type', this.form.type);
          formData.append('status', this.form.status);
          this.$axios({
            method: 'post',
            url: '/manager/addManager',
            data: formData,
          })
              .then((res) => {
                console.log("🟡 FULL RESPONSE:", res.data);
                console.log("🟡 FormData being sent:");
                for (let [key, value] of formData.entries()) {
                  console.log(`${key}: ${value}`);
                }

                if(res.data.errno===0){
                  this.$message({
                    message: 'success',
                    type: 'success'
                  });
                  this.getAllCustomer()
                  this.form={ 
                    name: '',
                    password: '',
                    email: '',
                    type: '',
                    status: ''
                  }
                }else{
                  this.$message.error("failed")
                }
              })
              .catch((err) => {
                console.log(err);
              });
        }
      })
    },
    filterStatus(value,row){
      return row.status === value
    },
    filterType(value,row){
      return row.type === value
    },
    openDeleteDialog() {
    this.getAllFixer(); // Refresh list just in case
    this.deleteDialogVisible = true;
    },
    confirmDelete(row) {
      this.deleteTarget = row;
      this.deleteConfirmVisible = true;
    },
    handleDelete() {
    const formData = new FormData();
    formData.append('managerId', this.deleteTarget.managerId);
    for (let pair of formData.entries()) {
      console.log(`${pair[0]}: ${pair[1]}`);
      console.log(this.deleteTarget);
    }
    this.$axios({
      method: 'post',
      url: '/manager/deleteManager',
      data: formData
    })
    .then((res) => {
      if (res.data.errno === 0) {
        this.$message.success('Deleted successfully');
        this.deleteConfirmVisible = false;
        this.getAllFixer(); // Refresh list
      } else {
        this.$message.error('Deletion failed');
      }
    })
    .catch(err => {
      console.log(err);
      this.$message.error('Server error');
    });
    },
  }
}
</script>

<style scoped>
.formBackground{
  box-shadow: 0px -4px 14px 0px #A6BADE;
}

.simple-search-content {
  position: relative;
  top:70px;
  right:50px;
}

.newButton{
  height: 40px;
  width: 100px ;
  font-size: 15px;
}

</style>
