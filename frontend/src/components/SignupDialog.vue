<!-- SignupDialog.vue -->
<template>
    <div class="signup-dialog" v-show="visible">
      <div class="signup-mask" @click="close"></div>
      
      <div class="signup-content">
        <div class="close-btn" @click="close">×</div>
        <h2 class="title">Sign Up</h2>
        
        <el-form :model="form" :rules="rules" ref="formRef">
          
          <el-form-item prop="username">
            <el-input v-model.trim="form.username" placeholder="Username (3-16 characters)"></el-input>
          </el-form-item>
  
          
          <el-form-item prop="email">
            <el-input v-model.trim="form.email" placeholder="Email">
              <template #append>
                <el-button 
                  :disabled="codeDisabled" 
                  @click="sendCode"
                >{{ codeBtnText }}</el-button>
              </template>
            </el-input>
          </el-form-item>
  
         
          <el-form-item prop="code">
            <el-input v-model.trim="form.code" placeholder="Verification code (6 digits)"></el-input>
          </el-form-item>
  
         
          <el-form-item prop="password">
            <el-input 
              v-model.trim="form.password" 
              type="password" 
              placeholder="Password (8-16 letters & numbers)"
              show-password
            ></el-input>
          </el-form-item>
  
          <el-button 
            type="primary" 
            class="submit-btn"
            :loading="loading"
            @click="handleSubmit"
          >Register</el-button>
        </el-form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: Boolean
    },
    data() {
      const validatePassword = (rule, value, callback) => {
        const reg = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{8,16}$/
        if (!reg.test(value)) {
          callback(new Error('Must contain uppercase, lowercase and numbers'))
        } else {
          callback()
        }
      }
  
      return {
        form: {
          username: '',
          email: '',
          code: '',
          password: ''
        },
        rules: {
          username: [
            { required: true, message: 'Required', trigger: 'blur' },
            { min: 3, max: 16, message: '3-16 characters', trigger: 'blur' }
          ],
          email: [
            { required: true, message: 'Required', trigger: 'blur' },
            { type: 'email', message: 'Invalid email', trigger: ['blur', 'change'] }
          ],
          password: [
            { required: true, message: 'Required', trigger: 'blur' },
            { validator: validatePassword, trigger: 'blur' }
          ]
        },
        codeBtnText: 'Get Code',
        codeDisabled: false,
        countdown: 0,
        loading: false
      }
    },
    methods: {
      handleScroll() {
    if (this.visible) {
      document.body.style.overflow = 'hidden'; 
    } else {
      document.body.style.overflow = '';
    }
  },watch: {
  visible(newVal) {
    this.handleScroll();
  }
},


beforeDestroy() {
  document.body.style.overflow = '';
},
      close() {
        this.$emit('update:visible', false)
      },
      async sendCode() {
  try {
    await this.$refs.formRef.validateField('email');
    this.codeDisabled = true;


    const formData = new FormData();
    formData.append('email', this.form.email); 


    await this.$axios.post(
      '/user/registerEmail', 
      formData, 
      {
        headers: {
          'Content-Type': 'multipart/form-data' 
        }
      }
    );

    this.startCountdown();
    this.$message.success('Verification code sent');
  } catch (err) {
    console.error('Error:', err.response?.data);
    this.codeDisabled = false;
    this.$message.error(err.response?.data?.message || 'Failed to send code');
  }
},
      startCountdown() {
        this.countdown = 60
        const timer = setInterval(() => {
          if (this.countdown <= 0) {
            clearInterval(timer)
            this.codeBtnText = 'Resend'
            this.codeDisabled = false
            return
          }
          this.codeBtnText = `${this.countdown}s`
          this.countdown--
        }, 1000)
      },
      async handleSubmit() {
        
  try {
    
    await this.$refs.formRef.validate();
    this.loading = true
    const formData = new FormData();
    formData.append('username', this.form.username);
    formData.append('email', this.form.email);
    formData.append('code', this.form.code);
    formData.append('password', this.form.password);
    const res = await this.$axios.post('/user/register', formData, {
      headers: {
        'Content-Type': 'multipart/form-data' 
      }
    });
    console.log('后端响应数据:', res.data) 
    
   
    if (res.data.errno === 0) {
      this.$message.success(res.data.msg || 'Registration successful')
      this.close()
      this.$emit('auto-fill', {
        email: this.form.email,
        password: this.form.password
      })
    } else {
     
      this.$message.error(res.data.msg || 'Registration failed')
    }
  } catch (err) {
    console.error('请求错误详情:', err)
   
    const serverMsg = err.response?.data?.msg
    const netError = err.message || 'Network Error'
    this.$message.error(serverMsg || netError)
  } finally {
    this.loading = false
  }
}
    }
  }
  </script>
  
  <style scoped>

.signup-dialog {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex; 
  justify-content: center; 
  align-items: center; 
  z-index: 9999;
}


.signup-content {
  position: relative;
  width: 90%;
  max-width: 420px;
  min-width: 300px; 
  padding: 30px 25px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  overflow-y: auto; 
  max-height: 90vh; 
}

  .el-form {
    margin-top: 20px;
  }
  
  .el-form-item {
    margin-bottom: 22px;
  }
  
  .el-input,
  .el-button {
    width: 100%;
  }
  
  .submit-btn {
    margin-top: 10px;
  }
  

  .title {
    text-align: center;
    margin: 0 0 15px;
    font-size: 24px;
    color: #333;
  }
  
 
  .close-btn {
    line-height: 1;
    top: 12px;
    right: 15px;
  }
  </style>