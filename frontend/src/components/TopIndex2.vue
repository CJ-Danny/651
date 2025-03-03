<template>
  <div class="Search">
    <div class="topIndex">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
               text-color="#8A8A8A" active-text-color="#40577D" style="border-top-right-radius: 10px;">

        <el-menu-item :index=(index+1).toString() v-for="(item, index) in data">
          <img :src=item.src style="height: 16px;" />&nbsp;{{item.title}}
        </el-menu-item>
        <!-- <el-menu-item index="2">
          <img src="../../../assets/管理员端/statistics/icon1.png" style="height: 20px;" />&nbsp;访客数据
        </el-menu-item> -->
        <div style="float: right;border-top-right-radius: 10px;position: relative; right: 4vw;top:18px;display: flex;align-items: center">
          <div>
            管理员ID: {{this.$store.state.adminID}}
          </div>
<!--          <el-button icon="el-icon-right" style="border: none;margin-left: 10px" @click="logout">退出登录</el-button>-->
        </div>
      </el-menu>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "TopIndex",
  props: {
    data: { type: Array },
    type: { type: Number},
  },
  data() {
    return {
      activeIndex: '', // 顶部导航栏控制
      // dt: [
      //   {src: require('../assets/管理员端/statistics/icon0.png'), title: '未处理工单'},
      //   {src: require('../assets/管理员端/statistics/icon1.png'), title: '未处理工单'}
      // ]
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      if (this.type === 1) {
        if (key === '1') {
          this.$router.push("/app/manager/people/customer")
        } else if (key === '2') {
          this.$router.push("/app/manager/people/manager")
        } else if (key === '3') {
          this.$router.push("/app/manager/people/maintainer")
        }
      }
      else if (this.type === 2) {
        if (key === '1') {
          this.$router.push("/app/manager/room/rooms")
        }
        else if (key === '2') {
          this.$router.push("/app/manager/room/roomsDetail")
        }
        else if (key === '3') {
          this.$router.push("/app/manager/room/rentRequests")
        }
      }
      else if (this.type === 3) {
        if (key === '1') {
          this.$router.push({path: "/app/manager/repair/repairlist", query:{type:"0"}})
        }
        else if (key === '2') {
          this.$router.push({path: "/app/manager/repair/repairlist", query:{type:"1"}})
        }
      }
      else if (this.type === 4) {
        if (key === '1') {
          this.$router.push("/app/manager/statistics/repair")
        }
        else if (key === '2') {
          this.$router.push("/app/manager/statistics/visitor")
        }
      }
    },
    logout() {
      this.$confirm('此操作将退出登录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(() => {
        this.$store.commit('set_token', '');
        this.$store.commit('set_userState', -1);
        this.$store.commit('set_userType', -1);
        this.$message({
          message: '退出登录!',
          type: 'success',
          duration: 1000,
        });
        this.$router.push('/login')
      }).catch((err) => {
        console.log(err);
      });
    }
  },
  mounted() {
    if(this.type === 1) {
      if (this.$route.path === '/app/manager/people/customer') {
        this.activeIndex = '1'
      } else if (this.$route.path === '/app/manager/people/manager' ) {
        this.activeIndex = '2'
      } else if (this.$route.path === '/app/manager/people/maintainer' ) {
        this.activeIndex = '3'
      }
    }
    else if(this.type === 2) {
      if (this.$route.path === '/app/manager/room/rooms') {
        this.activeIndex = '1'
      } else if (this.$route.path === '/app/manager/room/roomsDetail') {
        this.activeIndex = '2'
      } else if (this.$route.path === '/app/manager/room/rentRequests'){
        this.activeIndex = '3'
      }
    }
    else if(this.type === 3) {
      if (this.$route.query.type === '0') {
        this.activeIndex = '1'
      } else {
        this.activeIndex = '2'
      }
    }
    else if(this.type === 4) {
      if (this.$route.path === '/app/manager/statistics/repair') {
        this.activeIndex = '1'
      } else if (this.$route.path === '/app/manager/statistics/visitor') {
        this.activeIndex = '2'
      }
    }
  },
}
</script>

<style scoped>
.Search {
  height: 100%;
}

.topIndex {
  height: 61px;
  width: auto;
  position: relative;
  padding-left: 4px;
}

.el-button:active {
  background: #126c9e !important;
  font-weight: bold;
}
/*按钮悬浮*/
.el-button:hover {
  background: #126c9e !important;
  color: white !important;
  font-weight: bold;
  border-color: #01a8f9 !important;
}

.el-button:focus {
  background: #126c9e !important;
  color: white !important;
  font-weight: bold;

  border-color: #01a8f9 !important;
}
</style>
