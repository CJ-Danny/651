<template>
  <div style="background-color: rgb(250,252,255);overflow-x: hidden">
    <el-row>
      <el-col :span="18" style="margin-left: 2%;margin-top: 1%">
        <div style="color: rgb(32, 33, 36);font-family: zeitung, sans-serif;
    margin-bottom: 16px;font-size: 30px;margin-left: 50px;
    line-height: 44px;
    font-weight: 700;">
          Manager List
          <br/>
          <div style="display: flex;align-items: start">
             <span style="color: black;font-size: 15px;line-height: 24px;margin-top: 30px;
    font-weight: 400;">
          <span style="color: red">&nbsp;{{count || 0}}&nbsp;</span> Manager in total.
                  </span>
          </div>

        </div>

      </el-col>
      <el-col :span="5">
        <img src="../../../assets/login/logo-login-new.png" style="height: 70px;position: relative;top: 30px">

        <div class="simple-search-content" style="height: 4px;position: relative;top:30px;left:-100px">
          <el-input  v-model="searchInput" @keyup.enter.native="searchForManager"
                     style="width: 20vw;font-size: 16px;font-weight: 600;height: 40px">


            <el-button  slot="append" @click="searchForManager()"><img src="../../../assets/peopleManagement/icon4.png"
                                                                          style="position: relative;right: 5px;top:1px;height: 20px;" /></el-button>
          </el-input>
        </div>

      </el-col>
    </el-row>
    <img src="../../../assets/peopleManagement/1.png" style="height: 55vh;margin-bottom: -55vh;position: relative;left: 60vw;top:5vh">

    <div class="formBackground" style="width: 45vw;background-color: white;height: 72vh;margin-left: 5vw;margin-top: 0vh;

border-top-left-radius: 20px;border-top-right-radius: 20px;display: flex;flex-direction: column;align-items: center">
      <div style="height: 20px"></div>
      <el-table
          :data="tableData.slice((table_page - 1) * 7, table_page * 7)"
          style="width: 42vw;margin-left: 2.5vw;margin-top: 2vh">
        <el-table-column
            label="序号"
            width="130">
          <template slot-scope="scope">
            {{scope.$index+1}}

          </template>
        </el-table-column>
        <el-table-column
            label="姓名"
            prop="trueName"
            width="180">

        </el-table-column>
        <el-table-column
            label="联系电话"
            prop="phoneNumber"
            width="280">

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
  name: "manager",
  data(){
    return{
      count:'',
      allData:[],
      searchInput:'',
      editVisible:false,
      checkVisible:false,
      table_page:1,
      formLabelWidth: '120px',
      tableData: [],

    }
  },
  created() {
    this.getAllManager()
  },
  methods:{
    getAllManager(){
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      this.$axios({
        method: 'post',
        url: '/usermanage/managerCheck',
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
    searchForManager(){
      this.tableData=[]
      for (var i =0;i<this.allData.length;i++){
        if(this.allData[i].trueName.includes(this.searchInput)||
            this.allData[i].phoneNumber.includes(this.searchInput)
        )
          this.tableData.push(this.allData[i])
      }
    },
    filterStatus(value,row){
      return row.status === value
    },
    filterType(value,row){
      return row.type === value
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




</style>
