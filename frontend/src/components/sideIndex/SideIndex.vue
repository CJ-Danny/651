<template>
  <div class="SideIndex">
    <ul>
      <li @click="toHome()"><img class="logo" style="cursor: pointer;width: 50px;margin-left: 4px;"
          src="../../assets/管理员端/logo.png" />
      </li>
      <UserIndex v-if="type == 1" ></UserIndex>
      
      <RepairIndex v-else-if="type == 3"></RepairIndex>
      <li @click="toLogOut()" style="position: absolute; bottom: 50px;">
        <el-tooltip effect="dark" content="log out" placement="top">
          <img class="list12" style="cursor: pointer; position: relative; left: 21px;"
            src="../../assets/管理员端/logout.png" /><br>
        </el-tooltip>
      </li>
    </ul>
  </div>
</template>

<script>
import UserIndex from "@/components/sideIndex/UserIndex.vue"
import RepairIndex from "@/components/sideIndex/RepairIndex.vue"
export default {
  name: "SideIndex",
  components: {  UserIndex, RepairIndex },
  data() {
    return {
      type: 1, // 1user, 2admin, 3repair
    }
  },
  methods: {
    toLogOut() {
      this.$confirm('Log out of your account?', 'Notice', {
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        type: 'warning',
      }).then(() => {
        this.$store.commit('set_token', '');
        this.$store.commit('set_userState', -1);
        this.$store.commit('set_userType', -1);
        this.$message({
          message: 'log out!',
          type: 'success',
          duration: 1000,
        });
        this.$router.push('/login')
      }).catch((err) => {
        console.log(err);
      });
    },
    toHome() {
      this.$router.push('/')
    }
  },
  created() {
    if(this.$store.state.userState === 1 && this.$store.state.userType === 1) {
      this.type = 2
    } else if(this.$store.state.userState === 0) {
      this.type = 1
    } else if(this.$store.state.userState === 1 && (this.$store.state.userType === 2 || this.$store.state.userType === 3 || this.$store.state.userType === 4)) {
      this.type = 3
    }
  }
}
</script>

<style scoped>
.SideIndex {
  position: fixed;
  background-color: #78AAF0;
  display: inline-block;
  width: 92px;
  height: 96vh;
  min-height: 550px;
  margin-top: 2vh;
  overflow: hidden;
  padding: 0;
}

ul {
  margin: 0;
  list-style-type: none;
  padding-left: 0;
  padding-top: 15px;
  /* 4vh */
  padding-bottom: 15px;
  /* 4vh */
  width: 86px;
  background-color: #21232F;
  /* position: relative; */
  height: 100%;
  /* overflow: auto; */
  z-index: 1;
  display: flex;
  flex-direction: column;
  /* justify-content: space-around; */
  position: relative;
}

li img.logo {
  /* width: 5vw; */
  position: relative;
  left: 10px;
  z-index: 3;
}

li img.list12 {
  /* width: 3vw; */
  position: relative;
  left: 20px;
  /* margin-top: 45px; 7vh */
  width: 33px;
}
</style>
