<template>
  <div class="app">
    <li id="list1" @click="toList1()">
      <img class="list12" src="../../assets/管理员端/人员.png" /><br>
      <p style="font-size: 14px;position: relative;left: 10px;">People</p>
    </li>
    <li id="list2" @click="toList2()">
      <img class="list12" src="../../assets/管理员端/icon7.png" /><br>
      <p style="font-size: 14px;position: relative;left: 15px;">Room</p>
    </li>
    <li id="list3" @click="toList3()">
      <el-badge :value="missionNum" :max="10" :hidden="missionNum === 0" class="item"></el-badge>
        <img class="list3" src="../../assets/管理员端/icon3.png" /><br>

      <p style="font-size: 14px;position: relative;left: 15px;">Apply</p>
    </li>
    <li id="list4" @click="toList4()">
      <img class="list4" src="../../assets/管理员端/icon2.png" /><br>
      <p style="font-size: 14px;position: relative;left: 20px;">Repair</p>
    </li>
    <li id="list5" @click="toList5()">
      <img class="list12" src="../../assets/管理员端/icon6.png" /><br>
      <p style="font-size: 14px;position: relative;left: 15px;">Library</p>
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
      list2: undefined,
      list3: undefined,
      list4: undefined,
      list5: undefined,
      index: 1,
      missionNum: 0,
    }
  },
  methods: {
    //Set Blue card
    setCardPosition() {
      if (this.index === 1) {
        this.card.style.top = "-50px"
      } else if (this.index === 2) {
        this.card.style.top = "44px"
      } else if (this.index === 3) {
        this.card.style.top = "139px"
      } else if (this.index === 4) {
        this.card.style.top = "244px"
      } else if(this.index === 5) {
        this.card.style.top = "334px"
      }
    },

    init() {
      this.card = document.getElementById("card")
      this.list1 = document.getElementById("list1")
      this.list2 = document.getElementById("list2")
      this.list3 = document.getElementById("list3")
      this.list4 = document.getElementById("list4")
      this.list5 = document.getElementById("list5")
      var str = this.$route.path.split("/")[3]
      if (str == "people") {
        this.index = 1
      } else if (str == "room") {
        this.index = 2
      } else if (str == "apply") {
        this.index = 3
      } else if (str == "repair") {
        this.index = 4
      } else if(str == 'knowledge') {
        this.index = 5
      }
      this.initNotice()
      this.setCardPosition()
    },
    toList1() {
      this.$router.push('/app/manager/people/customer')
    },

    /*
    toList2() {
      this.$router.push('/app/manager/room/rooms')
    },
    */
   
    toList3() {
      this.$router.push({ path: "/app/manager/apply/applyList", query: { type: "0" } })
    },

    toList4() {
      this.$router.push('/app/manager/repair')
    },

    toList5() {
      this.$router.push('/app/manager/knowledge')
    },

    toHome() {
      this.$router.push('/')
    },
  },
  mounted() {
    this.init();
  },
  watch: {
    $route(to, from) {
      const url = to.name
      if (url === 'customerManagement' || url === 'managerManagement' || url === 'maintainerManagement') {
        this.index = 1
        this.setCardPosition();
        this.card.style.transition = "all 700ms ease 0s"
      } else if (url === 'rooms' || url === 'roomsDetail' || url === 'rentRequests') {
        this.index = 2
        this.setCardPosition();
        this.card.style.transition = "all 700ms ease 0s"
      } else if (url === 'applyList') {
        this.index = 3
        this.setCardPosition();
        this.card.style.transition = "all 700ms ease 0s"
      } else if (url === 'repair' || url === 'visitor') {
        this.index = 4
        this.setCardPosition();
        this.card.style.transition = "all 700ms ease 0s"
      } else if(url === 'knowledgeManager') {
        this.index = 5
        this.setCardPosition();
        this.card.style.transition = "all 700ms ease 0s"
      }
    }
  }
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

#list3 {
  margin-left: 4px;
  cursor: pointer;
  position: relative;
  top: 80px;
  left: -2px;
}

#list4 {
  margin-left: 4px;
  cursor: pointer;
  position: relative;
  top: 120px;
  left: -2px;
}

#list5 {
  margin-left: 6px;
  cursor: pointer;
  position: relative;
  top: 160px;
  left: -2px;
}

li {
  color: #fff;
  position: relative;
  height: auto;
}

li.list5 {
  margin-left: 20px;
  cursor: pointer;
  position: relative;
  top: 170px;
  left: -2px;
  z-index: 3;
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

li img.logo {
  /* width: 5vw; */
  position: relative;
  left: 10px;
  z-index: 3;
}

li img.share {
  width: 40px;
  position: relative;
  left: 2px;
}

li img.list12 {
  /* width: 3vw; */
  position: relative;
  left: 20px;
  /* margin-top: 45px; 7vh */
  width: 33px;
}

li img.list3 {
  position: relative;
  left: 15px;
  /* margin-top: 45px; 7vh */
  width: 41px;
}

li img.list4 {
  position: relative;
  left: 15px;
  /* margin-top: 45px; 7vh */
  width: 41px;
}

/* 分割线 */
ul hr {
  width: 40px;
  z-index: 3;
  position: relative;
  left: 20px;
  /* top: 40px; 4vh */
  opacity: 0.75;
}

li img.list4 {
  position: relative;
  left: 25px;
  /* margin-top: 80px; 12vh */
  width: 30px;
}

li img.list5 {
  /* position: relative; */
  /* left: 23px; */
  /* margin-top: 4vh; */
  width: 32px;
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

.item {
  z-index: 4;
  position: absolute;
  left: 40px;
  top: -5px;
}
</style>
