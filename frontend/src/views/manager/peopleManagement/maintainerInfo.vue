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
             <span style="color: black;font-size: 15px;line-height: 24px;margin-top: 30px;
    font-weight: 400;">
          <span style="color: red">&nbsp;{{count || 0}}&nbsp;</span> Serviceman in total.
                  </span>
            <img src="../../../assets/peopleManagement/时间管理04.png" style="height: 15vh;">
          </div>

        </div>

      </el-col>
      <el-col :span="5">
        <img src="../../../assets/login/logo-login-new.png" style="height: 70px;position: relative;top: 30px">

        <div class="simple-search-content" style="height: 4px;position: relative;top:30px;left:-100px">
          <el-input  v-model="searchInput" @keyup.enter.native="searchForMaintainer"
                     style="width: 20vw;font-size: 16px;font-weight: 600;height: 40px">

            <el-button  slot="append" @click="searchForMaintainer()"><img src="../../../assets/peopleManagement/icon4.png"
                                                                        style="position: relative;right: 5px;top:1px;height: 20px;" /></el-button>
          </el-input>
        </div>

      </el-col>
    </el-row>

    <div class="formBackground" style="width: 85vw;background-color: white;height: 65vh;margin-left: 5vw;

border-top-left-radius: 20px;border-top-right-radius: 20px;display: flex;flex-direction: column;align-items: center">
      <div style="height: 20px"></div>
      <el-table
          :data="tableData.slice((table_page - 1) * 7, table_page * 7)"
          style="width: 78vw;margin-left: 2.5vw;margin-top: 2vh">
        <el-table-column
            label="Number"
            width="130">
          <template slot-scope="scope">
          {{scope.$index+1}}

          </template>
        </el-table-column>
        <el-table-column
            label="Name"
            prop="trueName"
            width="180">

        </el-table-column>
        <el-table-column
            label="Phone Number"
            prop="phoneNumber"
            width="300">

        </el-table-column>
        <el-table-column
            prop="type"
            label="maintaince type"
            width="260"
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
            width="250"
            >
          <template slot-scope="scope">
            <el-tag
                :type="scope.row.status ? 'success' : 'danger'"
                disable-transitions><div v-if="scope.row.status" >Avalible</div>
              <div v-if="!scope.row.status">Unavailable</div>
            </el-tag>
          </template>
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
      searchInput:'',
      editVisible:false,
      checkVisible:false,
      table_page:1,
      formLabelWidth: '120px',
      tableData: [
      ],

    }
  },
  created() {
    this.getAllFixer()
  },
  methods:{
    getAllFixer(){
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      this.$axios({
        method: 'post',
        url: '/usermanage/fixerCheck',
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
    searchForMaintainer(){
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
