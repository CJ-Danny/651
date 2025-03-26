<template>
<div style="background-color: rgb(250,252,255);">
  <el-row>
    <el-col :span="18" style="margin-left: 2%;margin-top: 1%">
      <div style="color: rgb(32, 33, 36);font-family: zeitung, sans-serif;
    margin-bottom: 16px;font-size: 30px;margin-left: 50px;
    line-height: 44px;
    font-weight: 700;">
        Apartment Tenants List
        <br/>
        <span style="color: black;font-size: 15px;line-height: 24px;font-weight: 400;">
          <span style="color: red">&nbsp;{{count || 0}}&nbsp;</span> Registered Tenants in total
        </span>
      </div>
      
      <div style="display: flex;align-items: center">
        <el-button type="primary" class="newButton" @click="dialogFormVisible = true" style="margin-left: 50px">New</el-button>
        <el-upload
            class="upload-demo"
            :action=uploadFileUrl
            :http-request="uploadFile"
            :limit="1"
            :file-list="fileList"
            :show-file-list="false">
          <el-button size="primary" type="primary" style="margin-left: 20px">Import</el-button>
        </el-upload>
        <el-button class="button1" icon="el-icon-download" type="text" @click="download">Download Information Template</el-button>
      </div>

      <el-dialog title="Create New Tenant" :visible.sync="dialogFormVisible" >
        <el-form :model="form" :rules="formRules" ref="formRef">
          <el-form-item prop="userName" label="User name" :label-width="formLabelWidth">
            <el-input v-model="form.userName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="userPsd" label="Password" :label-width="formLabelWidth">
            <el-input v-model="form.userPsd" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="trueName" label="Contact Name" :label-width="formLabelWidth">
            <el-input v-model="form.trueName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="phoneNumber" label="Phone Number" label-width="125px">
            <el-input v-model="form.phoneNumber" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="email" label="Email" :label-width="formLabelWidth">
            <el-input v-model="form.email" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item prop="isInvitor" label="Identity" :label-width="formLabelWidth">
            <el-select v-model="form.isInvitor" placeholder="Please select an identity">
              <el-option label="Contact" value=0></el-option>
              <el-option label="Invitor" value=1></el-option>
            </el-select>
          </el-form-item>

        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">Cancle</el-button>
          <el-button type="primary" @click="handleCreate">Ok</el-button>
        </div>
      </el-dialog>
    </el-col>
    
    <el-col :span="5">
        <img src="../../../assets/login/logo-login-new.png" style="height: 70px;position: relative;top: 30px">

      <div class="simple-search-content" style="height: 4px;position: relative;top:30px;left:-100px">
        <el-input  v-model="searchInput" @keyup.enter.native="searchForCustomer"
                  style="width: 20vw;font-size: 16px;font-weight: 600;height: 40px">

          <el-button  slot="append" @click="searchForCustomer()"><img src="../../../assets/peopleManagement/icon4.png"
                                                                style="position: relative;right: 5px;top:1px;height: 20px;" /></el-button>
        </el-input>
      </div>

    </el-col>
  </el-row>

<div class="formBackground" style="width: 85vw;background-color: white;height: 65vh;margin-left: 5vw;
margin-top: 5vh;
border-top-left-radius: 20px;border-top-right-radius: 20px;display: flex;flex-direction: column;align-items: center">
  <div style="height: 20px;"></div>
  <el-table
      :data="tableData.slice((table_page - 1) * 6, table_page * 6)"
      style="width: 75vw;;margin-top: 2vh;">
    <el-table-column
        label="Id"
        prop="userId"
        min-width="30">

    </el-table-column>

    <el-table-column
        label="UserName"
        prop="userName"
        min-width="80">

    </el-table-column>

    <el-table-column
        label="Email"
        prop="email"
        min-width="100">

    </el-table-column>

    <el-table-column
        label="TotalBills"
        prop="rent_num"
        min-width="30">

    </el-table-column>

    <el-table-column
        label="UnpaidBills"
        prop="bill_unpaid_num"
        min-width="30">

    </el-table-column>

  </el-table>
  <div style="">
    <el-pagination
        layout="prev, pager, next"
        :total="tableData.length"
        :current-page.sync="table_page"
        :page-size="6"
    >
    </el-pagination>
  </div>
<div style="height: 1vh"></div>
</div>
</div>

</template>

<script>
export default {
  name: "customerInfo",
  data(){
    var checkPhone = (rule, value, callback) => {
      if (!value  || value === '') {
        return callback(new Error('Phone number cant be empty'));
      } else {
        var reg = /^1[0-9]{10}$/;
        if (!reg.test(value)) {
          callback(new Error('Not a valid Phone number'));
        } else {
          callback();
        }
      }
    };
    var checkEmail = (rule,value,callback) =>{
      if (!value  || value === '') {
        return callback(new Error('Email Address cant be empty'));
      } else {
        var reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!reg.test(value)) {
          callback(new Error('Invalid Email'));
        } else {
          callback();
        }
      }
    }
    return{
      uploadFileUrl:'http://18.117.136.172:8001/api/rs/file/upload',
      checkCustomerID:'',
      count:'',
      fileList:[],
      propertyDate:'',
      searchInput:'',
      propertyVisible:false,
      editVisible:false,
      dialogFormVisible:false,
      checkVisible:false,
      table_page:1,
      form: {
        legalPerson:'',
        companyName:'',
        phoneNumber:'',
        trueName:'',
        isInvitor:'',
        userName:'',
        userPsd:'',
        email:'',
      },
      allData:[],
      editForm:{
        legalPerson:'',
        companyName:'',
        phoneNumber:'',
        userID:'',
        userName:'',
        userPsd:'',
        trueName:'',
        email:'',
      },
      formLabelWidth: '120px',
      tableData: [],
      customerState:{
        isRent:false,
        rentList:[]
      },
      formRules:{
        phoneNumber:[
          {required:true,validator: checkPhone, trigger: 'blur'}
        ],
        userName:[
          { required: true, message: 'Please enter username', trigger: 'blur' },
        ],
        userPsd:[
          { required: true, message: 'Pleaes Enter password', trigger: 'blur' },
          { min: 2, max: 10, message: 'Password length needs to be [2,10]', trigger: 'blur' }
        ],
        trueName:[
          { required: true, message: 'Please Enter contact name', trigger: 'blur' },
        ],

        isInvitor:[
          { required: true, message: 'Please enter Identity', trigger: 'blur' },
        ],
        email:[
          {required:true,validator: checkEmail, trigger: 'blur'}
        ]

      },
      editFormRules:{
        phoneNumber:[
          {required:true,validator: checkPhone, trigger: 'blur'}
        ],
        userName:[
          { required: true, message: 'Please enter username', trigger: 'blur' },
        ],
        trueName:[
          { required: true, message: 'Please enter contact name', trigger: 'blur' },
        ],
        isInvitor:[
          { required: true, message: 'Please create identity', trigger: 'blur' },
        ],
        email:[
          {required:true,validator: checkEmail, trigger: 'blur'}
        ],
        customerID:'',

      }
    }
  },
  created() {
    this.getAllCustomer()
  },
  watch:{
    checkVisible:function(newval,oldval){
      this.propertyDate=''
      if(newval===false){
        var all=this.customerState.rentList.length
        for(var i=0;i < all;i++){
          this.$refs[`popover-` + i].doClose()
        }
      }
    }
  },
  methods:{
    pCancel(id) {
      this.pClose(id)
    },
    pClose(id) {
      this.$refs[`popover-` + id].doClose()
      this.propertyDate=''
    },
    pOpen(id){
      var all=this.customerState.rentList.length
      for(var i=0;i < all;i++){
        this.$refs[`popover-` + i].doClose()
      }
      this.$refs[`popover-` + id].doShow()
    },
    download(){
      window.open("http://10.251.254.210:8001/api/media/files/template.xlsx")
    },
    uploadFile(file){
      const formData = new FormData();
      formData.append('file', file.file);
      this.$axios({
        method: 'post',
        url: this.uploadFileUrl,
        data: formData,
      }).then(res => {
        console.log(JSON.stringify(res.data))
        if(res.data.errno===0){
          this.$message.success("Success")
          this.fileList=[]
          this.getAllCustomer()
        }else{
          this.$message.error(res.data.msg)
        }
      })
    },
    handleCreate(){
      this.$refs.formRef.validate((valid) =>{
        if(valid){
          this.dialogFormVisible=false
          const formData = new FormData();
          formData.append('token', this.$store.state.token);
          formData.append('legalPerson', this.form.legalPerson);
          formData.append('companyName', this.form.companyName);
          formData.append('phoneNumber', this.form.phoneNumber);
          formData.append('trueName', this.form.trueName);
          formData.append('userName', this.form.userName);
          formData.append('userPsd', this.form.userPsd);
          formData.append('email', this.form.email);
          formData.append('isInvitor', this.form.isInvitor);
          this.$axios({
            method: 'post',
            url: '/usermanage/newUser',
            data: formData,
          })
              .then((res) => {
                if(res.data.errno===0){
                  this.$message({
                    message: 'success',
                    type: 'success'
                  });
                  this.getAllCustomer()
                  this.form=[]
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
    getAllCustomer(){
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      this.$axios({
        method: 'post',
        url: '/manager/getUserInfo',
        data: formData,
      })
          .then((res) => {
            // window.alert(JSON.stringify(res.data))
            this.tableData=res.data.data
            this.count=this.tableData.length
            this.allData=res.data.data
          })
          .catch((err) => {
            console.log(err);
          });
    },
    filterTag(value, row) {
      return row.isInvitor === value;
    },
    searchForCustomer(){
      this.tableData=[]
      for (var i =0;i<this.allData.length;i++){
        if(this.allData[i].legalPerson.includes(this.searchInput)||
            this.allData[i].companyName.includes(this.searchInput)||
          this.allData[i].trueName.includes(this.searchInput)||
        this.allData[i].phoneNumber.includes(this.searchInput)
        )
          this.tableData.push(this.allData[i])
      }
    },

    handleEdit(number,row){
      this.editVisible=true
      this.editForm.legalPerson=row.legalPerson
      this.editForm.userID=row.userID
      this.editForm.companyName=row.companyName
      this.editForm.trueName=row.trueName
      this.editForm.phoneNumber=row.phoneNumber
      this.editForm.userName=row.userName
      this.editForm.userPsd=row.userPsd
      this.editForm.email=row.email


    },
    getRow(number,row){
      this.customerID=row.userID
    },

    saveEdit(){
      this.$refs.editFormRef.validate((valid) =>{
        if(valid){
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      formData.append('userID',this.editForm.userID);
      formData.append('legalPerson', this.editForm.legalPerson);
      formData.append('companyName', this.editForm.companyName);
      formData.append('phoneNumber', this.editForm.phoneNumber);
      formData.append('trueName', this.editForm.trueName);
      formData.append('userName', this.editForm.userName);
      formData.append('email', this.editForm.email);

          if (this.editForm.userPsd!==null)
        formData.append('userPsd', this.editForm.userPsd);
      formData.append('isInvitor', this.editForm.isInvitor);
      this.$axios({
        method: 'post',
        url: '/usermanage/editUserBasicInfo',
        data: formData,
      })
          .then((res) => {
            if(res.data.errno===0){
              this.$message({
                message: 'Edit success',
                type: 'success'
              });
              this.editVisible=false
              this.getAllCustomer()
            }

          })
          .catch((err) => {
            console.log(err);
          });}
    })},
    handleCheck(number,row){
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      formData.append('userID',row.userID)
      // window.alert(row.userID)
      this.checkCustomerID=row.userID
      this.$axios({
        method: 'post',
        url: '/usermanage/state',
        data: formData,
      })
          .then((res) => {
            // window.alert(JSON.stringify(res.data))
            this.customerState=res.data.data
            this.checkVisible=true

          })
          .catch((err) => {
            console.log(err);
          });
    }
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

.button1{
  margin-left: 20px;
  color: grey;
}
</style>
