<template>
  <div class="app">
    <li id="list1" @click="toList1()">
      <img class="list12" src="../../assets/管理员端/icon3.png" /><br>
      <p style="font-size: 14px;position: relative;left: 7px;">我的工单</p>
    </li>
    <li id="list2" @click="toList2()">
      <img class="list12" src="../../assets/管理员端/icon2.png" /><br>
      <p style="font-size: 14px;position: relative;left: 15px;">知识库</p>
    </li>
    <div class="card" id="card">
      <div class="upradius"></div>
      <div class="cardContent"></div>
      <div class="downradius"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'adminIndex',
  data() {
    return {
      card: undefined,
      list1: undefined,
      // list2: undefined,
      index: 1,
    }
  },
  methods: {
    // 组件数据初始化调用函数 TODO: 用户端
    init() {
      // console.log(this.$store.state.userState)
      // console.log(this.$store.state.userType)
      this.list1 = document.getElementById("list1")
      this.list2 = document.getElementById("list2")
      this.card = document.getElementById("card")
      var str = this.$route.path.split("/")[4]
      if (str.includes("repairlist")) {
        this.index = 1
      } else if (str === "knowledge") {
        this.index = 2
      }
      this.setCardPosition()
    },
    toList1() {
      this.index = 1
      this.setCardPosition();
      this.card.style.transition = "all 700ms ease 0s"
      this.$router.push({ path: "/app/manager/repair/repairlist", query: { type: "0" } })
    },
    //设置蓝色卡片的位置
    setCardPosition() {
      if (this.index === 1) {
        this.card.style.top = "-50px"
      } else if (this.index === 2) {
        this.card.style.top = "44px"
      }
    },
    // 去房间管理界面
    toList2() {
      this.index = 2
      this.setCardPosition();
      this.card.style.transition = "all 700ms ease 0s"
    this.$router.push('/app/manager/repair/knowledge')
    },
  },
  mounted() {
    this.init();
  },
}
</script>
<style scoped>
.app {
  position: relative;
  top: 60px;
  height: 480px;
  padding: 0;
  margin: 0;
}

#list1 {
  margin-left: 4px;
  cursor: pointer;
  position: relative;
  left: -2px;
}

#list2 {
  margin-left: 4px;
  cursor: pointer;
  position: relative;
  top: 40px;
  left: -2px;
}

li {
  color: #fff;
  position: relative;
  height: auto;
}

li p {
  display: block;
  position: relative;
  z-index: 3;
  margin: 0;
  /* z-index只有在position为relative, absolute 或者 fixed是才有效 */
}

li img {
  z-index: 3;
}

li img.list12 {
  /* width: 3vw; */
  position: relative;
  left: 20px;
  /* margin-top: 45px; 7vh */
  width: 33px;
}

.card {
  position: absolute;
  width: 86px;
  z-index: 2;
}

.upradius {
  z-index: 2;
  width: 86px;
  height: 40px;
  background-image: url(../../assets/管理员端/upradius.png);
}

.cardContent {
  height: 86px;
  width: 86px;
  background-color: #78AAF0;
  border-top-left-radius: 24px;
  border-bottom-left-radius: 24px;
}

.downradius {
  z-index: 2;
  width: 86px;
  height: 40px;
  background-image: url(../../assets/管理员端/downradius.png);
}
</style>
