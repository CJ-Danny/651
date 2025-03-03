


<template>
  <div>
    <div class="top">
      <img src="../assets/login/logo-login-new.png" style="width: 200px;height: 100%;margin-left: 30px">
      <div class="register-hint" @click="showSignup = true">
      <span class="register-link">Sign up now</span>
    </div>
    
    <SignupDialog 
      v-if="showSignup"
      :visible.sync="showSignup"
      @auto-fill="handleAutoFill"
    />
      <div class="home-page" @click="toHome">
        Welcome Page
      </div>
    </div>
    <img src="../assets/login/page2-1.png" class="img1" style="width: 400px;">
    
    <div class="bottom">
     
      <div class="main">
        <div class="container" id="b-container">
          <el-form class="form" :model="loginForm" :rules="loginFormRules" ref="loginFormRef">
            <h2 class="form_title title">Log in</h2>
            <div class="switch-state">
              <div class="manager active" @click="changeUserState(1)">Administrator</div>
              <div class="simple-user" @click="changeUserState(0)">User</div>
            </div>
            <el-form-item prop="email" class="username-item">
              <el-input v-model.trim="loginForm.email" 
            placeholder="email"
            class="form__input"
            autocomplete="off"
            @keyup.enter.native="login('loginForm')"></el-input>
            </el-form-item>
            <el-form-item prop="password" class="password-item">
              <el-input v-model="loginForm.password"
                        type="password"
                        placeholder="password"
                        class="form__input"
                        autocomplete="off"
                        @keyup.enter.native="login('loginForm')"></el-input>
            </el-form-item>
            <button class="form__button button submit" type="button" @click="login">Log in</button>
            
          </el-form>

          
        </div>
        <div class="switch" id="switch-cnt">
          <div class="switch__circle"></div>
          <div class="switch__circle switch__circle--t"></div>
          <div class="switch__container" id="switch-c2">

            <h2 class="switch__title title">Welcome back !</h2>
            <p class="switch__description description">Welcome to the WAT Property Management System. Please log in with your personal information</p>

          </div>
        </div>
      </div>
    </div>

  </div>
  
</template>

<script>
import SignupDialog from '@/components/SignupDialog.vue'
export default {

  
  name: "login",
  components: {
    SignupDialog
  },
  data() {
    var checkEmail = (rule, value, callback) => {
  if (!value || value === '') {
    return callback(new Error('email should not be empty'));
  } else {
    var reg = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!reg.test(value)) {
      callback(new Error('Please enter a vaild email'));
    } else {
      callback();
    }
  }
};
    let validatePass = (rule, value, callback) => {
      if (!value  || value === '') {
        callback(new Error('Please enter the password'));
      } else {
        let reg_pwd = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$/;
        if (!reg_pwd.test(value)) {
          callback(new Error('Password must be 8-18 characters long and include letters and numbers'));
        } else {
          // if (this.regForm.password2 !== '') {
          //   this.$refs.regForm.('password2');
          // }
          callback();
        }
      }
    };
    return {
      showSignup: false,
      userState: 1,
      loginForm:{
        email: '',
        password: ''
      },
      loginFormRules:{
        email:[
          {validator: checkEmail, trigger: 'blur'}
        ],
        // password:[
        //   {validator: validatePass, trigger: 'blur'}
        // ],
      },
    }
  },

  methods: {
    toHome() {
      this.$router.push('/')
    },
    
    
    handleAutoFill({ email, password }) {
      this.loginForm.email = email;
      this.loginForm.password = password;
    },
    changeUserState(state) {
      if(this.userState !== state) {
        const active = document.querySelector(".active")
        const manager = document.querySelector(".manager")
        const user = document.querySelector(".simple-user")
        active.classList.toggle("active")
        if(state === 1)
          manager.classList.toggle("active")
        else
          user.classList.toggle("active")
        this.userState = state
      }
    },
    login(formName) {
      const formData = new FormData();
    
      formData.append("email", this.loginForm.email); 
      formData.append("password", this.loginForm.password);
      formData.append("type", this.userState);
      this.$refs.loginFormRef.validate((valid) => {
        if (valid) {
          this.$axios({
            method: 'post',
            url: 'user/login',
            data: formData,
          })
              .then(res => {
                console.log(res);
                if(res.data.errno===0) {
                  this.$message.success('Successfully log in！');
                  this.$store.commit('set_token', res.data.token.replaceAll('\'', ''));
                  this.$store.commit('set_userState', this.userState);
                  this.$store.commit('set_userType', res.data.type);
                  this.$store.commit('set_adminID', res.data.id);
                  // this.$store.commit('set_is_login', true);
                  if(this.userState === 1) {
                    if(res.data.type === 1) {
                      setTimeout(() => {
                        this.$router.push('/app/manager/people/customer');
                      }, 1000);
                    }
                    else if(res.data.type === 2 || res.data.type === 3 || res.data.type === 4) {
                      setTimeout(() => {
                        this.$router.push({path: "/app/manager/repair/repairlist", query:{type:"0"}})
                      }, 1000);
                    }
                  }
                  else {
                    if(res.data.type === 0) {
                      setTimeout(() => {
                        this.$router.push('/app/client/userinfo');
                      }, 1000);
                    }
                    else if(res.data.type === 1) {
                      setTimeout(() => {
                        this.$router.push('/app/client/userinfo');
                      }, 1000);
                    }
                  }
                }
                else{
                  this.$message.error(res.data.msg);
                }
              })
              .catch(err => {
                console.log(err);
              })
        } else {
          console.log('Submission failed!!');
          return false;
        }
      });
    },
  }
}
</script>

<style scoped>
.top-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start; 
  padding: 20px 30px;
}

.logo-section {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.logo-img {
  width: 200px;
  height: auto;
  margin-bottom: 15px; 
}

.register-hint {
  margin: 0;
  align-self: center; 
}

.register-link {
  font-size: 16px; 
  font-weight: 600;
  padding: 8px 15px;
  border-radius: 8px;
  transition: all 0.3s;
}

.register-link:hover {
  background: rgba(75, 112, 226, 0.1);
}



.home-page {
  
  margin-top: 15px; 
}
*, *::after, *::before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  user-select: none;
}

.register-hint {
  cursor: pointer;
  margin-top: 20px;
}

.register-link {
  color: #4B70E2;
  text-decoration: underline;
}
.top{
  height: 8vh;
  position: relative;
  width: 100%;
  background-color: #ecf0f3;
  box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.register-hint {
  margin-top: 20px;
  font-size: 14px;
  color: #606266;
}

.register-link {
  color: #4B70E2;
  text-decoration: none;
  font-weight: 500;
  margin-left: 5px;
}

.register-link:hover {
  text-decoration: underline;
}

.home-page {
  width: 100px;
  height: 70%;
  margin-right: 50px;
  border-radius: 12px;
  box-shadow: 0 2px 6px 0 rgba(161, 161, 161, 0.4);
  color: rgb(75, 112, 226);
  font-size: 14px;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.img1 {
  position: absolute;
  bottom: 0;
  left: 0;
  z-index: 100;
}

.bottom {
  width: 100%;
  display: flex;
  height: 92vh;
  justify-content: center;
  align-items: center;
  font-family: "Montserrat", sans-serif;
  font-size: 12px;
  background-color: #ecf0f3;
  color: #a0a5a8;
}

.main {
  position: relative;
  width: 70%;
  min-width: 900px;
  min-height: 600px;
  height: 600px;
  background-color: #ecf0f3;
  box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
  border-radius: 12px;
  overflow: hidden;
  z-index: 1;
  display: flex;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 60%;
  height: 100%;
  padding: 25px;
  background-color: #ecf0f3;
  z-index: 100;
}

.form {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
  margin-left: 3%;
}

.switch-state {
  width: 30%;
  height: 30px;
  display: flex;
  justify-content: space-between;
  font-size: 16px;
  color: rgb(65, 80, 88);
  cursor: pointer;
}

.manager:hover, .simple-user:hover{
  color: rgb(22, 132, 252);
}

.active {
  border-bottom: 2px solid rgb(22, 132, 252);
  color: rgb(22, 132, 252);
}

.form__input /deep/ .el-input__inner {
  width: 350px;
  height: 40px;
  margin-top: 20px;
  padding-left: 25px;
  font-size: 13px;
  letter-spacing: 0.15px;
  /*border: none;*/
  outline: none;
  font-family: "Montserrat", sans-serif;
  background-color: #ecf0f3;
  transition: 0.25s ease;
  border-radius: 8px;
  box-shadow: inset 2px 2px 4px #d1d9e6, inset -2px -2px 4px #f9f9f9;
}

.form__input /deep/ .el-input__inner:focus {
  box-shadow: inset 4px 4px 4px #d1d9e6, inset -4px -4px 4px #f9f9f9;
}

.title {
  font-size: 34px;
  font-weight: 700;
  line-height: 3;
  color: #181818;
}

.description {
  font-size: 14px;
  letter-spacing: 0.25px;
  text-align: center;
  line-height: 1.6;
}

.button {
  width: 180px;
  height: 50px;
  border-radius: 25px;
  margin-top: 50px;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 1.15px;
  background-color: #4B70E2;
  color: #f9f9f9;
  box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #f9f9f9;
  border: none;
  outline: none;
  cursor: pointer;
}

.switch {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: 100%;
  width: 40%;
  padding: 50px;
  z-index: 200;
  background-color: #ecf0f3;
  overflow: hidden;
  box-shadow: 4px 4px 10px #d1d9e6, -4px -4px 10px #f9f9f9;
}

.switch__circle {
  position: absolute;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background-color: #ecf0f3;
  box-shadow: inset 8px 8px 12px #d1d9e6, inset -8px -8px 12px #f9f9f9;
  bottom: -60%;
  left: -60%;
}
.switch__circle--t {
  top: -30%;
  left: 60%;
  width: 300px;
  height: 300px;
}
.switch__container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  position: absolute;
  width: 400px;
  padding: 50px 55px;
}
.img1 { 
  z-index: 1 !important;
}

.top, .bottom {
  position: static; 
  z-index: auto;
}
</style>
