<template>
  <div class="app">
    <li id="list1" @click="toList1()">
      <img class="list12" src="../../assets/管理员端/人员.png" /><br>
      <p style="font-size: 14px;position: relative;left: 7px;">Personal Info</p>
    </li>
    <li id="list2" @click="toList2()">
      <img class="list12" src="../../assets/管理员端/icon2.png" /><br>
      <p style="font-size: 14px;position: relative;left: 10px;">Repair</p>
    </li>
    <li id="list3" @click="toList3()">
      <img class="list12" src="../../assets/管理员端/icon7.png" /><br>
      <p style="font-size: 14px;position: relative;left: 10px;">Rental Request</p>
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
      
      index: 1,
    }
  },
  methods: {
   
    setCardPosition() {
      if (this.index === 1) {
        this.card.style.top = "-50px"
      } else if (this.index === 2) {
        this.card.style.top = "80px"
      }
      else if (this.index === 3) {
        this.card.style.top = "208px"
      }
    },
    
    init() {
      // console.log(this.$store.state.userState)
      // console.log(this.$store.state.userType)
      this.card = document.getElementById("card")
      this.list1 = document.getElementById("list1")
      this.list2 = document.getElementById("list2")
      this.list3 = document.getElementById("list3"); 
      var str = this.$route.path.split("/")[3]
      if (str == "userinfo") {
        this.index = 1
      } else if (str == "repairment") {
        this.index = 2
      }
      else if (str === "room") { 
        this.index = 3;
      }
      this.setCardPosition()
    },
 
    toList1() {
      this.index = 1
      this.setCardPosition();
      this.card.style.transition = "all 700ms ease 0s"
      this.$router.push('/app/client/userinfo')
    },
   
    toList2() {
      this.index = 2
      this.setCardPosition();
      this.card.style.transition = "all 700ms ease 0s"
      this.$router.push('/app/client/repairment')
    },
    toList3() {
    this.index = 3;
    this.setCardPosition();
    this.card.style.transition = "all 700ms ease 0s";
    this.$router.push('/app/client/room'); 
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

#list3 {
  margin-left: 4px;
  cursor: pointer;
  position: relative;
  top: 100px;
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