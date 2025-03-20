<template>
  <div>
    <h2 style="margin-left: 3vw"> Maintenance Knowledge Base</h2>
    <el-input  v-model="searchInput" @keyup.enter.native="searchForKnowledge" placeholder="Search"
               style="width: 40vw;font-size: 16px;font-weight: 600;height: 40px;margin-left: 7vw;margin-bottom: 6vh;margin-top: 2vh">

      <el-button  slot="append" @click="searchForKnowledge()"><img src="../../../assets/peopleManagement/icon4.png"
                                                                  style="position: relative;right: 5px;top:1px;height: 20px;" /></el-button>
    </el-input>
    <div class="knowledgeBackground">
      <div style="margin-left: 2vw;margin-right: 2vw">
        <div style="height: 3vh"></div>
        <el-collapse v-model="activeNames" class="collapse-cls">
          <el-collapse-item v-for="(item, i) in showData" :title="'Problem: ' + item.problem" :name="i">
            <span style="color:#569675">Solution</span>
            {{item.solution}}
          </el-collapse-item>


          </el-collapse-item>
        </el-collapse>
      </div>

    </div>

  </div>

</template>

<script>
export default {
  name: "knowledge",
  data() {
    return {
      activeNames: [],
      searchInput: '',
      showData: [],
      allData: []
    }
  },
  created() {
    this.getAllKnowledge()
  },
  methods: {
    getAllKnowledge() {
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      this.$axios({
        method: 'post',
        url: '/manager/getAllKnowledge',
        data: formData,
      })
        .then((res) => {
          this.allData = res.data.data
          this.showData = this.allData
        })
        .catch((err) => {
          console.log(err);
        });
    },
    searchForKnowledge() {
      if (!this.searchInput.trim()) {
        this.showData = this.allData;
        return;
      }
      
      const formData = new FormData();
      formData.append('problem', this.searchInput);
      
      this.$axios({
        method: 'post',
        url: 'http://18.117.136.172:8000/api/manager/searchKnowledge',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Authorization': `Bearer ${this.$store.state.token}`
        },
        data: formData,
      })
        .then((res) => {
          if (res.data.errno === 0 && res.data.data) {
            this.showData = res.data.data;
          } else {
            this.showData = [];
          }
        })
        .catch((err) => {
          console.log(err);
          this.$message.error('Search failed. Please try again.');
        });
    }
  }
}
</script>

<style scoped>
.knowledgeBackground{
  width: 80vw;
  background-color: white;
  min-height: 75vh;
  margin-left: 7vw;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  box-shadow: 0px -4px 14px 0px #A6BADE;
}
.collapse-cls ::v-deep .el-collapse-item__header{
  color: #EF7C03;
  font-size: 17px;
  font-weight: bold;
}

.collapse-cls ::v-deep .el-collapse-item__content{
margin-left: 1vw;
}
</style>