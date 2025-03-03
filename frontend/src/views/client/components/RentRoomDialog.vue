<template>
  <el-dialog
    :title="'Apply to rent：' + rentRequestRoomList.length + ' rooms'"
    :visible.sync="showRentRequestVisible"
    width="40%"
  >
    <div style="font-weight: bold; font-size: 16px">Rental Order：</div>
    <div v-for="room in rentRequestRoomList" :key="room.id" style="margin-left: 5px">
      {{ room.floor }} floor · {{ room.roomNumber }} · {{ room.roomName }} · {{ room.area }} m² ·
      {{ room.rent }} CAD/month
    </div>
    <br />
    <el-form :model="rentRequestForm" ref="rentRequestFormRef">
      <div v-if="isRentRequestUserNotFound" style="color: red">The specified user was not found</div>
      <div v-else>{{ rentRequestUserInfo.trueName }}&nbsp;{{ rentRequestUserInfo.companyName }}</div>
      <el-form-item label="Rental time" required>
        <br />
        <el-col :span="11">
          <el-form-item prop="startTime" :rules="[{ required: true, message: 'Start date cannot be empty' }]">
            <el-date-picker
              type="date"
              placeholder="Select start date"
              v-model="rentRequestForm.startTime"
              style="width: 100%"
              value-format="yyyy-MM-dd 00:00:00"
            ></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">
          <div style="width: 100%; text-align: center">-</div>
        </el-col>
        <el-col :span="11">
          <el-form-item prop="endTime" :rules="[{ required: true, message: 'End date cannot be empty' }]">
            <el-date-picker
              type="date"
              placeholder="Select end date"
              v-model="rentRequestForm.endTime"
              style="width: 100%"
              value-format="yyyy-MM-dd 00:00:00"
            ></el-date-picker>
          </el-form-item>
        </el-col>
      </el-form-item>
    </el-form>
    <span slot="footer">
      <el-button @click="showRentRequestVisible = false">Cancel</el-button>
      <el-button type="primary" @click="sendRentRequest">Confirm</el-button>
    </span>
  </el-dialog>
</template>

<script>
  import qs from 'qs';
  export default {
    components: {},
    data() {
      return {
        showRentRequestVisible: false,
        rentRequestRoomList: [],
        rentRequestRoomIDList: [],
        rentRequestForm: {
          phoneNumber: '',
          startTime: '',
          endTime: '',
        },
        isRentRequestUserNotFound: false,
        rentRequestUserInfo: {
          userID: 0,
          trueName: '',
          companyName: '',
        },
      };
    },
    methods: {
      show(roomList) {
        this.showRentRequestVisible = true;
        this.rentRequestRoomList = roomList;
        this.rentRequestRoomIDList = roomList.map((room) => room.roomID);
        this.rentRequestForm = {
          phoneNumber: '',
          startTime: '',
          endTime: '',
        };
        this.clearRentRequestUserInfo();
      },
      sendRentRequest() {
  this.$refs['rentRequestFormRef'].validate((valid) => {
    if (valid) {
     
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      formData.append('roomId', this.rentRequestRoomIDList[0]); 
      formData.append('startTime', this.rentRequestForm.startTime);
      formData.append('endTime', this.rentRequestForm.endTime);

  
      this.$axios
        .post('/user/applyRoom', formData, {
          headers: {
            'Content-Type': 'multipart/form-data' 
          }
        })
        .then((res) => {
          if (res.data.errno === 0) {
            this.$message.success('Successfully Rent');
            this.showRentRequestVisible = false;
            setTimeout(() => this.$router.go(0), 500);
          } else {
            this.$message.error(res.data.msg);
          }
        })
        .catch((err) => {
          console.error('Error:', err.response?.data);
          this.$message.error('Request failed: ' + (err.response?.data?.message || 'Unknown error'));
        });
    }
  });
},
      clearRentRequestUserInfo() {
        this.isRentRequestUserNotFound = false;
        this.rentRequestUserInfo = {
          userID: 0,
          trueName: '',
          companyName: '',
        };
      },
    },
  };
</script>

<style scoped></style>
