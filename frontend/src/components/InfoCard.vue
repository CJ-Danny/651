<template>
  <div class="info-card">
    <div class="head-bg">
      <img src="@/assets/userInfo/head.jpg" alt="" />
    </div>
    <div style="position: relative;top: -40px;">
      <div class="avatar-border center">
        <div class="avatar"><img src="@/assets/userInfo/avatar.jpg" alt="" /></div>
      </div>
      <div class="name center">{{ name }}</div>
      <!-- <div class="sub-name center" style="margin-top: 40px"><img src="@/assets/userInfo/people.svg"
          style="height: 16px;margin-right: 3px;" />Name</div> -->
      <div class="sub-name center" style="margin-top: 20px">
        <!-- <img src="@/assets/userInfo/telephone.svg"
          style="height: 16px;margin-right: 3px;" /> -->
          {{ phone }}</div>
          
    </div>

    <!-- 邀请访客 -->
    <!-- <el-dialog title="邀请访客" :visible.sync="dialogFormVisible" style="text-align: left;">
      <el-form :model="form" :rules="rules">
        <el-form-item label="访客姓名" :label-width="formLabelWidth" prop="customerName">
          <el-input v-model="form.customerName" placeholder="请输入访客姓名"></el-input>
        </el-form-item>
        <el-form-item label="访客电话" :label-width="formLabelWidth" prop="phoneNumber">
          <el-input v-model="form.phoneNumber" placeholder="请输入访客电话"></el-input>
        </el-form-item>
        <el-form-item label="您的邮箱地址" :label-width="formLabelWidth" prop="email">
          <el-input v-model="form.email" placeholder="请输入邮箱地址"></el-input>
        </el-form-item>
        <el-form-item label="到访时间" :label-width="formLabelWidth" prop="time">
          <el-date-picker v-model="form.time" value-format="yyyy-MM-dd HH:mm:ss" type="datetimerange" range-separator="至"
            start-placeholder="开始日期" end-placeholder="结束日期">
          </el-date-picker>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </div>
    </el-dialog> -->
  </div>
</template>

<script>
export default {
  name: 'InfoCard',
  data() {
    // var checkPhone = (rule, value, callback) => {
    //   if (!value || value === '') {
    //     return callback(new Error('手机号不能为空'));
    //   } else {
    //     var reg = /^1[0-9]{10}$/;
    //     if (!reg.test(value)) {
    //       callback(new Error('请输入有效的手机号'));
    //     } else {
    //       callback();
    //     }
    //   }
    // };
    // var checkEmail = (rule, value, callback) => {
    //   if (!value || value === '') {
    //     return callback(new Error('邮箱地址不能为空'));
    //   } else {
    //     var reg = /^[a-zA-Z0-9]+([-_.][A-Za-zd]+)*@([a-zA-Z0-9]+[-.])+[A-Za-zd]{2,5}$/;
    //     if (!reg.test(value)) {
    //       callback(new Error('请输入有效的邮箱地址'));
    //     } else {
    //       callback();
    //     }
    //   }
    // };
    return {
      dialogFormVisible: false,
      formLabelWidth: '130px',
      form: {
        customerName: '',
        phoneNumber: '',
        email: '',
        time: null, // 2023-06-25 16:32:00
      },
      pickerOptions: {
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '明天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }
        ],
      },
      rules: {
        customerName: [
          { required: true, message: '请填写访客姓名', trigger: 'blur' }
        ],
        email: [
          { required: true, validator: checkEmail, trigger: 'blur' }
        ],
        phoneNumber: [
          { required: true, validator: checkPhone, trigger: 'blur' }
        ],
        time: [
          { required: true, message: '请填写到访时间', trigger: 'blur' }
        ],
      }
    }
  },
  props: {
    name: { type: String, default: '张三' },
    phone: { type: String, default: '114514' },
    lawperson: { type: String, default: "李四" },
  },
  methods: {
    submit() {
      var regPhone = /^1[0-9]{10}$/;
      var regEmail = /^[a-zA-Z0-9]+([-_.][A-Za-zd]+)*@([a-zA-Z0-9]+[-.])+[A-Za-zd]{2,5}$/;
      if (this.form.customerName === '' || this.form.email === '' || this.form.phoneNumber === '' || this.form.time === null) {
        this.$message({
          message: '表单信息不能为空!',
          type: 'error',
          duration: 1000,
        })
      } else if (!regPhone.test(this.form.phoneNumber)) {
        this.$message({
          message: '电话格式错误!',
          type: 'error',
          duration: 1000,
        })
      } else if (!regEmail.test(this.form.email)) {
        this.$message({
          message: '邮箱格式错误!',
          type: 'error',
          duration: 1000,
        })
      } else {
        let form = new FormData();
        form.append('token', this.$store.state.token);
        form.append('customerName', this.form.customerName)
        form.append('email', this.form.email)
        form.append('phoneNumber', this.form.phoneNumber)
        form.append('arrivalTime', this.form.time[0])
        form.append('leaveTime', this.form.time[1])
        this.$axios({
          method: 'post',
          url: 'inviter/inviteVisitor',
          data: form,
        })
          .then(res => {
            this.$message({
              message: res.data.msg,
              type: 'success',
              duration: 1000,
            })
            this.form.customerName = ''
            this.form.email = ''
            this.form.phoneNumber = ''
            this.form.time = null
            this.dialogFormVisible = false
          })
          .catch(err => {
            this.$message({
              message: res.data.msg,
              type: 'error',
              duration: 1000,
            })
          })
      }
    },
  }
}
</script>

<style scoped>
.info-card {
  text-align: center;
  height: 350px;
  width: 250px;
  border-radius: 1rem;
  background-color: #F6FAFF;
  color: black;
  padding: 10px;
  box-shadow: 0px 0px 8px 1px #E6E6E6;
}

.head-bg {
  z-index: 1;
  width: 100%;
  height: 100px;
  overflow: hidden;
  border-radius: .8rem;
}

.head-bg img {
  width: 100%;
}

.avatar-border {
  z-index: 2;
  background-color: rgba(255, 255, 255);
  height: 85px;
  width: 85px;
  border-radius: 50%;
  position: relative;
  left: 83px;
}

.avatar {
  z-index: 3;
  height: 75px;
  width: 75px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
}

.name {
  font-size: 20px;
  font-weight: bold;
}

.sub-name {
  font-size: medium;
  color: rgb(176, 186, 201);
}

.center {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
