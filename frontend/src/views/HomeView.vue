<template>
  <div class="homeBody">
    <div class="HomePage" id="box">
      <div class="Section_0">
        <div class="bg">
          <div class="logo">
            <img src="../assets/shiyilogo.png" alt="" style="height: 75px;position: relative; top: 10px;" />
          </div>
          <div class="content0">
            <div class="content0_title noSelectFont">
              Waterloo Apartment
            </div>
            <div class="content_text">
              <div class="content_left">
                <h1 class="noSelectFont property-title">Property Management System</h1>
                <div class="start_button_content">
                  <button class="start-button anime" style="background-color: rgb(237,238,244)" @click="startNow()">
                    Use Now
                  </button>
                </div>
              </div>
              <div class="content_middle"></div>
              
              <div class="content_right noSelectFont" style="display: flex; flex-wrap: wrap; gap: 20px;">

                <div class="heritage">Work Order Dispatch Workflow,Implement an Integrated Service Workflow</div>
                <div class="heritage">Visualized Room Information,Boosting Quality of Life Significantly</div>
                <div class="heritage">Apartment User Management,Enhance Property Service Quality</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="Section_1 noSelectFont">
        <transition name="head">
          <div class="Section_1_Head" v-show="isShow1">
            <h1>Property Maintenance System</h1>
            <p>——Service Process is Controllable, Service Workflow is Traceable</p>
          </div>
        </transition>
        <transition name="left1">
          <div class="Section_1_Left" v-show="isShow1">
            <div class="Section_1_Left-content">
              <div class="Section_1_Left_content-left">
                <img src="../assets/homepage/list.png" alt="" />
              </div>
              <div class="Section_1_Left_content-right">
                <div style="position: relative; right: 12px; top: 3px">
                  Water Shutoff? Contact Waterloo Apartment Property Management!
                </div>
                <div style="margin-top: 16px; position: relative; right: 20px">
                  Power outage in your room? Contact Waterloo Apartment Property Management!
                </div>
                <div style="margin-top: 14px; position: relative; right: 5px">
                Mechanical failure? Just contact Waterloo Apartment Property Management!
                </div>
                <div style="margin-top: 10px; position: relative; right: 10px">
              Anytime, Any Issue, Just Contact Waterloo Apartment Property Management!
                </div>

              </div>
            </div>
            <div class="Section_1_Left-content1">
              <div class="Section_1_Left_content-left1">
                <img src="../assets/homepage/list.png" alt="" />
              </div>
              <div class="Section_1_Left_content-right1">
                <div style="position: relative; right: 12px; top: 6px">
                  Waterloo Apartment Property Management offers sincere and dedicated service!
                </div>
                <div style="margin-top: 16px; position: relative; right: 20px">
                  Waterloo Apartment Property Management has professional business expertise!
                </div>
                <div style="margin-top: 10px; position: relative; right: 5px">
                  Waterloo Apartment Property has a comprehensive service workflow!
                </div>
                <div style="margin-top: 14px; position: relative; right: 10px">
                  Waterloo Apartment Property Management – Providing You with World-Class Service!
                </div>
              </div>
            </div>
          </div>
        </transition>
        <transition name="right1">
          <div class="Section_1_right" v-show="isShow1">
            <img src="../assets/homepage/Section1-right.png" alt="" />
          </div>
        </transition>
      </div>
      <div class="Section_2" noSelectFont>
        <transition name="head">
          <div class="Section_2_Head" v-show="isShow2">
            <h1>Client</h1>
            <p>——Unified access across multiple channels to fully meet customer needs</p>
          </div>
        </transition>
        <transition name="left2">
          <div class="Section_2_Left" v-show="isShow2">
            <div class="NumberRoll">
              <!-- <NumberRoll :from="StartNumberRoll1" :to="NumberRoll1" /> -->
              <CountTo ref="refcountofore1" :start-val="StartNumberRoll1" :end-val="NumberRoll1" :duration="1000">
              </CountTo>
            </div>
            <div class="NumberRollTitle">Number of customers</div>
            <div class="NumberRoll">
              <!-- <NumberRoll :from="StartNumberRoll2" :to="NumberRoll2" /> -->
              <CountTo ref="refcountofore2" :start-val="StartNumberRoll2" :end-val="NumberRoll2" :duration="1000">
              </CountTo>
            </div>
            <div class="NumberRollTitle">Number of maintenance personnel</div>
            <div class="NumberRoll">
              <!-- <NumberRoll :from="StartNumberRoll3" :to="NumberRoll3" /> -->
              <CountTo ref="refcountofore3" :start-val="StartNumberRoll3" :end-val="NumberRoll3" :duration="1000">
              </CountTo>
            </div>
            <div class="NumberRollTitle">Number of visitors</div>
          </div>
        </transition>
        <transition name="right2">
          <div class="Section_2_right" v-show="isShow2">
            <img src="../assets/homepage/page2-1.png" style="height: 100%;" alt="" />
          </div>
        </transition>
      </div>
      <div class="Section_3">
        <transition name="head">
          <div class="Section_3_Head noSelectFont" v-show="isShow3">
            <h1>Employee side</h1>
            <p>——Service process is controllable, and service workflow is traceable</p>
          </div>
        </transition>
        <transition name="middle3">
          <div class="card-content" v-show="isShow3">
            <div class="cardApp">
              <div class="card-img image1">
                <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_wso9kgdi.json" background="transparent"
                  speed="1" style="width: 300px; height: 300px" loop autoplay></lottie-player>
              </div>
              <div class="card-info noSelectFont">
                <p class="text-title">Customer Management</p>
                <p class="text-body">Providing you with the best customer management platform！</p>
              </div>
              <div class="card-footer">
                <button class="radial-buttonSearch anime" style="background-color: #e3e3e3;position: relative;"
                  @click="adminRoute(0)">
                  Start!
                </button>
              </div>
            </div>
            <div class="cardApp">
              <div class="card-img image2">
                <lottie-player src="https://assets3.lottiefiles.com/packages/lf20_49rdyysj.json" background="transparent"
                  speed="1" style="width: 300px; height: 300px" loop autoplay></lottie-player>
              </div>
              <div class="card-info noSelectFont">
                <p class="text-title">Space and Personnel Management</p>
                <p class="text-body">Providing you with the best management platform—choosing us is the right decision!</p>
              </div>
              <div class="card-footer">
                <button class="radial-buttonData anime" style="background-color: #e3e3e3;position: relative;"
                  @click="adminRoute(1)">
                  Start!
                </button>
              </div>
            </div>
            <div class="cardApp">
              <div class="card-img image3">
                <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_noz9pzmw.json" background="transparent"
                  speed="1" style="width: 300px; height: 300px" loop autoplay></lottie-player>
              </div>
              <div class="card-info noSelectFont">
                <p class="text-title">Service Management</p>
                <p class="text-body">Providing you with the most comprehensive service management platform!</p>
              </div>
              <div class="card-footer">
                <button class="radial-buttonSI anime" style="background-color: #e3e3e3;position: relative;"
                  @click="adminRoute(2)">
                  Start!
                </button>
              </div>
            </div>
          </div>
        </transition>
      </div>
      <div class="Section_4 noSelectFont">
        <div style="width: 100%; min-height: 30vh"></div>
        <div class="AboutUs">
          <transition name="middle4">
            <div class="GetStart" v-show="isShow4">
              <div class="GetStartLeft">
                <div class="GetStartLeftTitle">Ready to get started?</div>
                <div class="GetStartLeftSubtitle">Go explore!</div>
              </div>
              <div class="GetStartRight">
                <div class="GetStartRightBlock">
                  <!-- btn ToRegisterButton hover-filled-slide-right -->
                  <!-- btn ToLoginButton hover-filled-slide-down -->
                  <button v-if="this.$store.state.userState === -1" class="radial-button2 anime" style="background-color: #23c6ba" @click="toLogin()">
                    Log in
                  </button>
                  <button v-else class="radial-button2 anime" style="background-color: #23c6ba" @click="startNow()">
                  start!
                  </button>
                </div>
              </div>
            </div>
          </transition>
          <transition name="middle4">
            <div class="OurInfo" v-show="isShow4">
              <div class="OurInfoTitle">
                <!-- <img src="../../assets/homepage/Hunting.png" alt="" /> -->
              </div>
              <div class="OurInfoContent">
                <div class="OurInfoContent2">
                  <h3>Contact us!</h3>
                  <div class="OurInfoContent2-content">
                    <div class="OurInfoContent2-left">
                      <img src="../assets/homepage/WeChatQRcode.png" alt="" />
                      <br /><span style="position: relative; top: 4px">Founder WhatsApp</span>
                    </div>
                    <div class="OurInfoContent2-right">

                      <div style="margin-top: 15px; position: relative; left: 30px; top: 20px;">
                        <span style="color: #9d9c9c">e-mail</span>&nbsp;<span>WAT@gmail.com</span>
                        <div style="height: 20px;"></div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="OurInfoContent3">
                  <h3>Developers</h3>
                  <div class="OurInfoContent3-block">
                    <div><span>Project Leader: Jikang He</span></div>
                    <div style="margin-top: 15px;">Frontend Development Team: Ruoyan Xu, Wenrui Zhao, Yue Fang</div>
                    <div style="margin-top: 15px;">Backend Development Team: Jikang He</div>
                    <div class="OurInfoContent3-block3">
                      <img src="../assets/homepage/Section4_foot.png" alt="" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CountTo from 'vue-count-to';
export default {
  name: 'HomeView',
  components: { CountTo },
  data() {
    return {
      nowPage: 0,
      box: undefined,
      isShow1: false,
      isShow2: false,
      isShow3: false,
      isShow4: false,
      StartNumberRoll1: 14,
      StartNumberRoll2: 21, // may change
      StartNumberRoll3: 0, // may change
      // StartNumberRoll4: 271793,
      NumberRoll1: 0,
      NumberRoll2: 0,
      NumberRoll3: 0,
      NumberRoll4: 0,
      input3: '',
      selectValue: '1',
      adviceVisible: false,
      advice: ''
    };
  },
  methods: {
    addEvent(obj, xEvent, fn) {
      if (obj.attachEvent) {
        obj.attachEvent('on' + xEvent, fn);
      } else {
        obj.addEventListener(xEvent, fn, false);
      }
    },
    pageUp() {
      if (this.nowPage === 4) {
        this.nowPage--;
        this.box.style.transform = 'translate3d(0, -300vh, 0)'; //'transform: translate3d(0, -100%, 0);transition: all 700ms ease 0s;'
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow4 = false;
        this.isShow3 = true;
      } else if (this.nowPage === 3) {
        this.nowPage--;
        this.box.style.transform = 'translate3d(0, -200vh, 0)'; //'transform: translate3d(0, -100%, 0);transition: all 700ms ease 0s;'
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow3 = false;
        this.isShow2 = true;
        this.NumberRoll1 = this.StartNumberRoll1;
        this.NumberRoll2 = this.StartNumberRoll2;
        this.NumberRoll3 = this.StartNumberRoll3;
        this.NumberRoll4 = this.StartNumberRoll4;
        this.StartNumberRoll1 = 0;
        this.StartNumberRoll2 = 0;
        this.StartNumberRoll3 = 0;
        this.StartNumberRoll4 = 0;
        
      } else if (this.nowPage === 2) {
      
        this.nowPage--;
        this.box.style.transform = 'translate3d(0, -100vh, 0)'; //'transform: translate3d(0, -100%, 0);transition: all 700ms ease 0s;'
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow2 = false;
        this.isShow1 = true;
        this.StartNumberRoll1 = this.NumberRoll1;
        this.StartNumberRoll2 = this.NumberRoll2;
        this.StartNumberRoll3 = this.NumberRoll3;
        this.StartNumberRoll4 = this.NumberRoll4;
        this.NumberRoll1 = 0;
        this.NumberRoll2 = 0;
        this.NumberRoll3 = 0;
        this.NumberRoll4 = 0;
       
        //console.log(nowPage)
      } else if (this.nowPage === 1) {
        this.nowPage--;
       
        this.box.style.transform = 'translate3d(0, 0, 0)'; //'transform: translate3d(0, -100%, 0);transition: all 700ms ease 0s;'
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow1 = false;
      
        //console.log(nowPage)
      }
    },
    pageDown() {
      if (this.nowPage === 0) {
       
        this.nowPage++;
        this.isShow1 = true;
        this.box.style.transform = 'translate3d(0, -100vh, 0)'; //'transform: translate3d(0, -100%, 0);transition: all 700ms ease 0s;'
        this.box.style.transition = 'all 700ms ease 0s';
        
        //console.log(nowPage)
      } else if (this.nowPage === 1) {
       
        this.nowPage++;
        this.box.style.transform = 'translate3d(0, -200vh, 0)'; //'transform: translate3d(0, -100%, 0);transition: all 700ms ease 0s;'
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow1 = false;
        this.isShow2 = true;
        this.NumberRoll1 = this.StartNumberRoll1;
        this.NumberRoll2 = this.StartNumberRoll2;
        this.NumberRoll3 = this.StartNumberRoll3;
        this.NumberRoll4 = this.StartNumberRoll4;
        this.StartNumberRoll1 = 0;
        this.StartNumberRoll2 = 0;
        this.StartNumberRoll3 = 0;
        this.StartNumberRoll4 = 0;
      
        //console.log(nowPage)
      } else if (this.nowPage === 2) {
        this.nowPage++;
        this.box.style.transform = 'translate3d(0, -300vh, 0)';
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow2 = false;
        this.isShow3 = true;
        this.StartNumberRoll1 = this.NumberRoll1;
        this.StartNumberRoll2 = this.NumberRoll2;
        this.StartNumberRoll3 = this.NumberRoll3;
        this.StartNumberRoll4 = this.NumberRoll4;
        this.NumberRoll1 = 0;
        this.NumberRoll2 = 0;
        this.NumberRoll3 = 0;
        this.NumberRoll4 = 0;
      } else if (this.nowPage === 3) {
        this.nowPage++;
        this.box.style.transform = 'translate3d(0, -400vh, 0)';
        this.box.style.transition = 'all 700ms ease 0s';
        this.isShow3 = false;
        this.isShow4 = true;
      }
    },
    pageToHome() {
      if (this.nowPage === 4) {
        this.pageUp();
      }
      if (this.nowPage === 3) {
        this.pageUp();
      }
      if (this.nowPage === 2) {
        this.pageUp();
      }
      if (this.nowPage === 1) {
        this.pageUp();
      }
    },
    pageToEnd() {
      if (this.nowPage === 0) {
        this.pageDown();
      }
      if (this.nowPage === 1) {
        this.pageDown();
      }
      if (this.nowPage === 2) {
        this.pageDown();
      }
      if (this.nowPage === 3) {
        this.pageDown();
      }
    },
    onMouseWheel(e) {
      var ev = e || window.event;
      var down = true;
      down = ev.wheelDelta ? ev.wheelDelta < 0 : ev.detail > 0;
      if (down) {
       
        this.pageDown();
        //console.log('---------')
      } else {
      
        this.pageUp();
        //console.log('++++++++++')
      }
      if (ev.preventDefault) {
     
        ev.preventDefault();
      }
      return false;
    },
    init() {
      this.box = document.getElementById('box');
      this.addEvent(this.box, 'mousewheel', this.onMouseWheel);
      this.addEvent(this.box, 'DOMMouseScroll', this.onMouseWheel);
      // Vanilla.init(document.querySelectorAll(".card-item"), {
      //   max: 25,
      //   speed: 400,
      // });
      let that = this;
      document.onkeydown = function (e) {
        let e1 = e || window.event || arguments.callee.caller.arguments[0];
        if (e1 && (e1.keyCode == 38 || e1.keyCode == 37 || e1.keyCode == 33)) {
          that.pageUp();
          e1.preventDefault();
        } else if (e1 && (e1.keyCode == 40 || e1.keyCode == 39 || e1.keyCode == 34)) {
          that.pageDown();
          e1.preventDefault();
        } else if (e1 && (e1.keyCode == 116 || e1.keyCode == 36)) {
          that.pageToHome();
          e1.preventDefault();
        } else if (e1 && e1.keyCode == 35) {
          that.pageToEnd();
          e1.preventDefault();
        }
      };
    },
    toLogin() {
      if (this.$store.state.userState === -1) {
        this.$router.push("/login")
      } else {
        this.$message({
          message: 'You are already logged in!',
          type: 'warning'
        });
      }

    },
    adminRoute(index) {
      
      if (this.$store.state.userState === 1 && this.$store.state.userType === 1) {
        if (index === 0) {
          this.$router.push('/app/manager/people/customer')
        } else if (index === 1) {
          this.$router.push('/app/manager/room/rooms')
        } else if (index === 2) {
          this.$router.push({ path: "/app/manager/repair/repairlist", query: { type: "0" } })
        }
      } else {
        this.$message({
          message: 'Only administrators can access this page!',
          type: 'warning'
        });
      }

    },
    startNow() {
      if (this.$store.state.userState === -1) {
        this.$router.push('/login')
      } else if (this.$store.state.userState === 0) {
        this.$router.push('/app/client/userinfo')
      } else if (this.$store.state.userState === 1 && this.$store.state.userType === 1) {
        this.$router.push('/app/manager/people/customer')
      } else if (this.$store.state.userState === 1 && (this.$store.state.userType === 2 || this.$store.state.userType === 3 || this.$store.state.userType === 4)) {
        this.$router.push({ path: "/app/manager/repair/repairlist", query: { type: "0" } })
      }
    }
  },
  mounted() {
    this.init();
  },
};
</script>

<style scoped>
.homeBody {
  overflow-x: hidden;
  overflow-y: scroll;
  scrollbar-width: none;
}

.homeBody::-webkit-scrollbar {
  display: none;
}

.property-title {
  font-size: 45px;
}


.bg {
  background: url('../assets/homepage/Page1.png');
  width: 100%;
  height: 100%;
  /* position: fixed; */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: 0;

}

.logo {
  position: absolute;
}

.login_button {
  border-radius: 7px;
  background-color: transparent;
  position: absolute;
  left: 80%;
  top: 3.5%;
  font-size: 15px;
  font-weight: bold;
  width: 95px;
  height: 40px;
}

.register_button {
  border-radius: 7px;
  position: absolute;
  left: 86.5%;
  top: 3.5%;
  font-size: 15px;
  font-weight: bold;
  width: 95px;
  height: 40px;
}

.en_font {
  position: absolute;
  left: 18%;
  top: 35%;
  font-weight: bold;
  font-size: 45px;
  line-height: 55px;
  color: #f3f7fa;
  font-family: 'Ubuntu';
}

.ch_font {
  position: absolute;
  left: 19%;
  top: 52%;
  font-size: 18px;
  color: #d0dbe5;
}

.inputbox {
  position: absolute;
  left: 18%;
  top: 66%;
  width: 44%;
}


button.anime {
  background-color: white;
  border: none;
  cursor: pointer;
}

button.radial-button {
  position: absolute;
  border-radius: 4px;
  left: 65%;
  top: 65.8%;
  font-size: 15px;
  font-weight: bold;
  width: 125px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: #081336;

  padding: 12px 40px;
}

.radial-button::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: gainsboro;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-button:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

button.radial-button1 {
  position: absolute;
  background-color: #0D1018;
  border: 1.5px solid #FFFFFF;
  border-radius: 5px;
  border-radius: 4px;
  left: 63%;
  top: 63%;
  font-size: 15px;
  font-weight: bold;
  width: 100px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: white;

}

.radial-button1::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #D2D3D7;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-button1:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

.hot_font {
  position: absolute;
  left: 24%;
  top: 74%;
  font-size: 16px;
  color: #d0dbe5;
  font-family: 'Microsoft YaHei';
}

#hey {
  margin: 3px auto 0;
  padding: 0;
  list-style: none;
  display: table;
  width: 200px;
  text-align: center;
}

.b {
  color: #fff;
  text-transform: uppercase;
  text-decoration: none;
  letter-spacing: 0.15em;
  display: inline-block;
  padding: 9px 10px;
  width: 60px;
  position: relative;
  cursor: pointer;
}

.b::before {
  background: none repeat scroll 0 0 transparent;
  bottom: 0;
  content: "";
  display: block;
  height: 2px;
  left: 90%;
  position: absolute;
  background: #fff;
  transition: width 0.3s ease 0s, left 0.3s ease 0s;
  width: 0;
}

.b:hover::before {
  width: 100%;
  left: 1%;
}

.arrow {
  position: absolute;
  left: 47%;
  top: 87%;
  width: 120px;
  cursor: pointer;
}

/* @font-face {
  font-family: 'Ubuntu';
  src: url('../../assets/fonts/UbuntuMono-B.ttf');
} */
</style>

<style scoped>


.noSelectFont {
  cursor: default;
}

.HomePage {
  height: 100vh;
  width: 100vw;
}


.Section_0 {
  /* min-width: 100%;
  min-height: 100%; */
  height: 100vh;
  width: 100vw;
  position: relative;
  /* overflow: hidden; */
}

.content0 {
  margin-left: 52%;
  position: relative;
  top: 25%;
  min-width: 540px;
  color: white;
}

.content0_title {
  position: relative;
  left: 300px;
  padding: 10px 20px;
  background-color: rgb(25, 44, 221);
  display: inline;
  font-size: 30px;
  font-weight: bold;
}

.content_text {
  display: flex;
}

.content_left {
  font-size: 32px;
}

.start_button_content {
  position: relative;
  left: 240px;
  bottom: 70px;
}

.content_middle {
  margin-left: 40px;
  margin-right: 30px;
  margin-top: 30px;
  width: 3px;
  height: 380px;
  background: white;
}

.content_right {
  overflow: hidden;
  display: flex;
  flex-wrap: wrap; 
  gap: 20px; 
}

.heritage {
  line-height: 1.5; 
  width: auto; 
  max-width: 300px; 
  margin-top: 20px;
  margin-right: 20px;
  white-space: normal; 
}


.Section_1 {
  background-image: url("@/assets/homepage/Section1-bg.jpg");
  background-size: cover;
  /* min-width: 100%;
  min-height: 100%; */
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}


.Section_2 {
  background-image: url("../assets/homepage/Section2-bg.jpg");
  background-size: cover;
  /* min-width: 100%;
  min-height: 100%; */
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.Section_3 {
  background-image: url("../assets/homepage/Section3-bg.png");
  background-image: linear-gradient(to bottom, #dfe9f3 0%, white 100%);
  /* background-color: #141723; */
  /* min-width: 100%;
  min-height: 100%; */
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}


.Section_0_Head {
  text-align: center;
  min-height: 0%;
}

.Section_1_Left {
  height: auto;
  width: 25vw;
  display: inline-block;
  position: relative;
  left: 10vw;
  top: 110px;
}

.Section_1_Left-content {
  display: flex;
  min-width: 400px;
}

.Section_1_Left-content1 {
  display: flex;            
  justify-content: center;  
  align-items: center;      
}


.Section_1_Left_content-left {
  margin-right: 20px;
}

.Section_1_Left_content-left1 {
  margin-right: 20px;
}


.Section_1_Left_content-right {
  font-size: 15px;
  text-align: center;
  padding-left: 50px;
}

.Section_1_Left_content-right1 {
  font-size: 15px;
  text-align: center;
  padding-left: 50px;
}

.Section_1_right {
  height: 20vh;
  width: 20vw;
  position: relative;
  /* top: 10vh;
  left: 28.6vw; */
  top: 5vh;
  left: 40vw;

  display: inline-block;
}

.Section_1_right img {
  max-height: 50vh;
}

.Section_2_Left {
  height: 20vh;
  width: 25vw;
  position: relative;
  top: 5vh;
  left: 15vw;
  display: inline-block;
}

.Section_2_right {
  height: 400px;
  position: relative;
  left: 30%;
  top: 13%;
  display: inline-block;
}

.Section_2_right img {
  max-height: 80vh;
}

.NumberRoll {
  line-height: 60px;
  font-size: 55px;
  color: #3C7FD9;
  font-family: "Ubuntu";
}

.NumberRollTitle {
  line-height: 30px;
  color: #ABABAB;
  margin-bottom: 5vh;
}

@keyframes leftAnimation {
  from {
    transform: translateX(-100%);
    opacity: 0.5;
  }

  to {
    transform: translateX(0%);
    opacity: 1;
  }
}

@keyframes rightAnimation {
  from {
    transform: translateX(100%);
    opacity: 0.5;
  }

  to {
    transform: translateX(0%);
    opacity: 1;
  }
}

@keyframes headAnimation {
  from {
    transform: scaleX(0.4) scaleY(0.4);
    opacity: 0;
  }

  to {
    transform: scaleX(1) scaleY(1);
    opacity: 1;
  }
}

@keyframes MiddleAnimation {
  from {
    transform: translateY(100px);
    opacity: 0;
  }

  to {
    transform: translateY(0%);
    opacity: 1;
  }
}

@keyframes HeadIndexAnimation {
  from {
    transform: translateY(-55px);
  }

  to {
    transform: translateY(0%);
  }
}

.headIndex-enter-active {
  animation: HeadIndexAnimation 0.6s linear;
}

.headIndex-leave-active {
  animation: HeadIndexAnimation 0.6s reverse linear;
}

.head-enter-active {
  animation: headAnimation 1s linear;
}

.head-leave-active {
  animation: headAnimation 1s reverse linear;
}

.left1-enter-active {
  animation: leftAnimation 1s;
}

.left1-leave-active {
  animation: leftAnimation 0.4s reverse;
}

.right1-enter-active {
  animation: rightAnimation 1s;
}

.right1-leave-active {
  animation: rightAnimation 0.5s reverse;
}

.left2-enter-active {
  animation: leftAnimation 1s;
}

.left2-leave-active {
  animation: leftAnimation 0.4s reverse;
}

.right2-enter-active {
  animation: rightAnimation 1s;
}

.right2-leave-active {
  animation: rightAnimation 0.5s reverse;
}

.middle3-enter-active {
  animation: MiddleAnimation 2s;
}

.middle3-leave-active {
  animation: MiddleAnimation 1s reverse;
}

.middle4-enter-active {
  animation: MiddleAnimation 2s;
}

.middle4-leave-active {
  animation: MiddleAnimation 1s reverse;
}

.Section_1_Head {
  color: #080b3b;
  text-align: center;
  /* margin-top: 10px; */
}

.Section_2_Head {
  color: #080b3b;
  text-align: center;
  /* margin-top: 100px; */
}

.Section_3_Head {
  /* color: #edededc5; */
  color: #080b3b;
  text-align: center;
  /* margin-top: 100px; */
}


.Section_4 {
  /* min-width: 100%;
  min-height: 100%; */
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.AboutUs {
  width: 100%;
  min-height: 70vh;
  background-image: url("@/assets/homepage/Section4_bg.png");
  background-position: center top;
  background-size: auto;
}

.GetStart {
  padding: 20px 40px;
  display: flex;
  margin: auto;
  min-width: 550px;
  height: 85px;
  width: 30%;
  background-color: white;
  border-radius: 6px;
  position: relative;
  bottom: 10vh;
  box-shadow: 3px 18px 27px 5px #E2EBFF;
  overflow: hidden;
}

.GetStartLeft {
  display: inline-block;
  min-width: 310px;
}

.GetStartLeftTitle {
  color: #3C7FD9;
  line-height: 42px;
  font-size: 30px;
  font-family: "ubuntu";
}

.GetStartLeftSubtitle {
  color: #A4ADB3;
  line-height: 23px;
  font-size: 18px;
  margin-top: 20px;
  font-family: 方正准圆;
}

.GetStartRight {
  /* display: inline-block; */
  min-width: 320px;
}

button.start-button {
  position: absolute;
  right: 310px;
  top: 15vh;
  border-radius: 4px;
  font-size: 18px;
  width: 160px;
  height: 50px;
  border-radius: 25px;
  overflow: hidden;
  z-index: 1;
  color: rgb(107, 160, 228);
  font-weight: bold;
  /*font color*/
  padding: 12px 40px;
  transition: all .5s;
}

.start-button::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #3B65F4;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.start-button:hover {
  color: white;
}

.start-button:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

button.radial-button2 {
  position: absolute;
  right: 310px;
  top: 100px;
  border-radius: 4px;
  font-size: 15px;
  width: 125px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: white;
  /*font color*/
  padding: 12px 40px;
}

.radial-button2::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #3B65F4;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-button2:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

button.radial-button3 {
  position: absolute;
  border-radius: 4px;
  top: 15vh;
  left: 30px;
  font-size: 15px;
  width: 125px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: white;
  /*font color*/
  padding: 12px 40px;
}

.radial-button3::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #23C6BA;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-button3:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

.GetStartRightBlock {
  margin-left: 320px;
  position: relative;
  bottom: 80px;
  min-width: 200px;
}

@keyframes HideAnimation {
  from {
    transform: translateY(10px);
    opacity: 0;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.Hide-enter-active {
  animation-name: HideAnimation 1s;
}

.Hide-leave-active {
  animation-name: HideAnimation 1s reverse;
}

.OurInfo {
  width: 100vw;
  position: relative;
}

.OurInfoTitle {
  margin-left: 10vw;
  margin-top: 5vh;
  margin-bottom: 2vh;
}

.OurInfoContent {
  margin-left: 10vw;
  width: 80vw;
  height: 32vh;
  min-height: 250px;
  padding: 20px;
  padding-top: 10px;
  border-radius: 5vh;
  box-shadow: 4px 6px 10px 4px #CEE9FA;
  overflow: hidden;
  display: flex;
  justify-content: space-around;
}

.OurInfoContent h3 {
  color: #3B76EF;
  font-weight: bold;
  font-size: 20px;
}

.OurInfoContent2-content {
  min-width: 310px;
  height: auto;
  display: flex;
  justify-content: space-between;
}

.OurInfoContent2-left {
  position: relative;
}

.OurInfoContent2-right {
  position: relative;
  right: 50px;
  bottom: 20px;
}

.OurInfoContent2-left img {
  height: 120px;
}



.OurInfoContent1 {
  display: inline-block;
}

.OurInfoContent1-block {
  position: relative;
  top: 3vh;
}

.OurInfoContent1-block1 {
  background-color: #CEE9FA;
  cursor: pointer;
  margin-left: 1.2vw;
  text-align: center;
  width: 14vw;
  height: 6vh;
  border-radius: 1.2vh;
}

.OurInfoContent1-block1:hover {
  opacity: 0.85;
}

.OurInfoContent1-block1 span {
  color: #1240A7;
  position: relative;
  font-size: 2vh;
  top: 1.5vh;
}

.OurInfoContent1-block2 {
  text-align: center;
  display: inline-block;
  margin-left: 1.2vw;
  margin-right: 1.5vw;
  position: relative;
  top: 4vh;
  cursor: pointer;
  background-color: #87B0E4;
  width: 6vw;
  height: 5vh;
  border-radius: 1vh;
}

.OurInfoContent1-block2:hover {
  opacity: 0.85;
}

.OurInfoContent1-block2 span {
  color: #FFFFFF;
  position: relative;
  font-size: 2vh;
  top: 0.75vh;
}

.OurInfoContent1-block3 {
  text-align: center;
  display: inline-block;
  background-color: #2B61CD;
  width: 6.5vw;
  height: 5vh;
  border-radius: 1vh;
  cursor: pointer;
  position: relative;
  top: 4vh;
}

.OurInfoContent1-block3:hover {
  opacity: 0.85;
}

.OurInfoContent1-block3 span {
  color: #FFFFFF;
  position: relative;
  font-size: 2vh;
  top: 0.75vh;
}

.OurInfoContent2 {
  display: inline-block;
  min-width: 400px;
}


.OurInfoContent3 {
  display: inline-block;
  min-width: 400px;
}

.OurInfoContent3-block1 {
  display: inline-block;
  text-align: center;
  min-width: 100px;
  height: 5vh;
  border-radius: 1vh;
  /* background-image: url(@/assets/homepage/block3-bg.png); */
  background-size: cover;
  position: relative;
  top: 3.5vh;
  margin-right: 60px;
  cursor: pointer;
}

.OurInfoContent3-block1:hover {
  opacity: 0.85;
}

.OurInfoContent3-block1 span {
  color: white;
  position: relative;
  top: 1.1vh;
  opacity: 0.9;
}

.OurInfoContent3-block2 {
  display: inline-block;
  text-align: center;
  min-width: 92px;
  height: 5vh;
  border-radius: 1vh;
  /* background-image: url(../assets/homepage/block3-bg.png); */
  background-size: cover;
  position: relative;
  top: 3.5vh;
  cursor: pointer;
}

.OurInfoContent3-block2:hover {
  opacity: 0.85;
}

.OurInfoContent3-block2 span {
  color: white;
  position: relative;
  top: 1.1vh;
  opacity: 0.9;
}

.OurInfoContent3-block3 {
  position: relative;
  top: 5vh;
}


.card-content {

  display: flex;
  justify-content: space-around;
  position: relative;
  top: 8vh;
}

.cardApp {
  width: 300px;
  height: 455px;
  padding: .8em;
  background: #f5f5f5;
  position: relative;
  overflow: visible;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  border-radius: 1rem;
}

.card-img {
  /* background-color: #ffcaa6; */
  height: 300px;
  width: 300px;
  border-radius: .5rem;
  transition: .3s ease;
}

.image1 {
  background-color: #c7c7fe;
}

.image2 {
  background-color: #fbd796;
}

.image3 {
  background-color: #b0eb97;
}

.card-info {
  padding-top: 5%;
}


.card-footer {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 10px;
  border-top: 1px solid #ddd;
}

/*Text*/
.text-title {
  font-weight: 900;
  font-size: 1.2em;
  line-height: 1.5;
  margin: 0;
}

.text-body {
  font-size: .9em;
  padding-bottom: 10px;
}

/*Hover*/
.card-img:hover {
  transform: translateY(-10%);
  /* box-shadow: rgba(226, 196, 63, 0.25) 0px 13px 47px -5px, rgba(180, 71, 71, 0.3) 0px 8px 16px -8px; */
}

button.radial-buttonSearch {
  position: absolute;
  border-radius: 4px;
  font-size: 15px;
  width: 125px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: #232323;
  font-family: 'Ubuntu';
  /*font color*/
  padding: 12px 40px;
}

.radial-buttonSearch::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #c7c7fe;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-buttonSearch:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

button.radial-buttonData {
  position: absolute;
  border-radius: 4px;
  font-size: 15px;
  width: 125px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: #232323;
  font-family: 'Ubuntu';
  /*font color*/
  padding: 12px 40px;
}

.radial-buttonData::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #fbd796;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-buttonData:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}

button.radial-buttonSI {
  position: absolute;
  border-radius: 4px;
  font-size: 15px;
  width: 125px;
  height: 42px;
  overflow: hidden;
  z-index: 1;
  color: #232323;
  font-family: 'Ubuntu';
  /*font color*/
  padding: 12px 40px;
}

.radial-buttonSI::before {
  content: '';
  position: absolute;
  z-index: -1;
  top: 100%;
  left: 50%;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  background-color: #b0eb97;
  transform-origin: center;
  transform: translate3d(-50%, -50%, 0) scale(0, 0);
  transition: transform 500ms ease-in-out;
}

.radial-buttonSI:hover::before {
  transform: translate3d(-50%, -50%, 0) scale(15, 15);
}
</style>
