<template>
  <div class="user-info">
    <div class="head">
      <div class="left"></div>
      <div class="right">

      </div>
    </div>
    <div class="content">
      <div class="title-image"><img src="@/assets/userInfo/bg.jpg" alt="" /></div>
      <div style="display: flex;">
        <div class="title-content center">
          Waterloo Apartment
        </div>
      </div>
      <div style="position: relative; top: -26px;">
        <div class="line" style="margin-bottom: 15px;"></div>
        <div class="introduction" style="text-align: center;">
        Stylish Modern Condo Within Walking Distance of University of Waterloo!
        </div>
        <div class="line" style="margin-top: 15px;"></div>
        <div class="show-info">
          <div class="card">
            <Card :name="trueName" :phone="phoneNumber" :lawperson="legalPerson"></Card>
          </div>
          <div class="info-content">
            <div class="info-content-info">
              <div class="sub-info"><img src="../../assets/userInfo/room.svg"
                  style="height: 22px; position: relative; top: 4px; right: 3px;margin-right: 2px;" />Your Room:
                <span v-if="roomNumber.length === 0">Currently no rented room</span>
                <span v-else>
                  <span v-for="(item, i) in roomNumber">{{ item }}<span v-show="i !== roomNumber.length - 1">, </span></span>
                </span>
              </div>
              <h3>Rental History</h3>
              <el-table :data="rentList" stripe style="width: 100%" empty-text="No rental history available">
                
                <el-table-column label="Room No." width="150">
                  <template slot-scope="scope">
                    <div class="room-number-list">
                      {{ scope.row.roomNumber }}
                    </div>
                  </template>
                </el-table-column>

                <el-table-column label="Start Date" width="200">
                  <template slot-scope="scope">
                    {{ scope.row.startTime ? scope.row.startTime.substring(0, 10) : 'N/A' }}
                  </template>
                </el-table-column>

                <el-table-column label="End Date" width="200">
                  <template slot-scope="scope">
                    {{ scope.row.endTime ? scope.row.endTime.substring(0, 10) : 'N/A' }}
                  </template>
                </el-table-column>

                <el-table-column label="Status" width="200" align="center">
                  <template slot-scope="scope">
                    <div style="cursor: default;">
                    <el-tag :type="getStatusType(scope.row.status)" style="width: 100px; text-align: center;">
                      {{ getStatusText(scope.row.status) }}
                    </el-tag>
                  </div>
                  </template>
                </el-table-column>

                <!-- <el-table-column label="Payment Due" width="160">
                  <template slot-scope="scope">
                    {{ scope.row.status === 0 ? getEndOfMonth() : 'Paid' }}
                  </template>
                </el-table-column> -->
              </el-table>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>



</template>

<script>
import Card from "@/components/InfoCard.vue";
export default {
  name: "UserInfo",
  components: { Card },
  data() {
    return {
      userID: 1,
      phoneNumber: 'undefined',
      trueName: 'undefined', // 联系人姓名
      companyName: 'undefined',
      legalPerson: 'undefined', // 法人代表
      introduction: 'undefined',
      roomNumber: [],
      rentList: [],
      customerState: {
        rentList: []
      },
    }
  },
  methods: {
    handleCheck(number, row) {
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      formData.append('userID', row.userID)
      this.$axios({
        method: 'post',
        url: '/usermanage/state',
        data: formData,
      })
        .then((res) => {
          this.customerState = res.data.data
          this.checkVisible = true

        })
        .catch((err) => {
          console.log(err);
        });
    },
    init() {
      const formData = new FormData();
      formData.append('token', this.$store.state.token)
      this.$axios({
        method: 'post',
        url: 'user/getHomeInfo',
        data: formData,
      })
        .then((res) => {
          console.log('API Response:', res.data);
          
          if (res.data.errno === 0 && res.data.data) {
            // Basic user info
            this.userID = res.data.data.userID || 1;
            this.phoneNumber = res.data.data.email || 'undefined';
            this.trueName = res.data.data.userName || 'undefined';
            
            // If your API doesn't return these fields, set defaults
            this.companyName = res.data.data.companyName || 'undefined';
            this.legalPerson = res.data.data.legalPerson || 'undefined';
            this.introduction = res.data.data.introduction || 'undefined';
            
            // Get room numbers - field might be different in your API
            this.roomNumber = [];
            if (res.data.data.rentList && res.data.data.rentList.length > 0) {
              // Extract room numbers from rentList
              this.roomNumber = res.data.data.rentList.map(rent => rent.roomNumber);
            }
            
            // Get rent list
            this.rentList = res.data.data.rentList || [];
          } else {
            console.error('API returned error:', res.data.errmsg || 'Unknown error');
            this.$message.error('Failed to load user information');
          }
        })
        .catch((err) => {
          console.error('API request failed:', err);
          this.$message.error('Failed to connect to server');
        })
    },

    getStatusType(status) {
      switch (status) {
        case 0:
          return 'warning'; // Yellow for pending
        case 1:
          return 'success'; // Green for approved
        case 2:
          return 'danger';  // Red for rejected
        default:
          return 'info';    // Default color
      }
    },

    getStatusText(status) {
      switch (status) {
        case 0:
          return 'Pending Review';
        case 1:
          return 'Approved';
        case 2:
          return 'Rejected';
        default:
          return 'Unknown Status';
      }
    }
    // getEndOfMonth() {
    //   const date = new Date();
    //   // Set to last day of current month
    //   const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
      
    //   // Format to YYYY-MM-DD
    //   const year = lastDay.getFullYear();
    //   const month = String(lastDay.getMonth() + 1).padStart(2, '0');
    //   const day = String(lastDay.getDate()).padStart(2, '0');
      
    //   return `${year}-${month}-${day}`;
    // }
  },
  mounted() {
    this.init()
  }
}


</script>
<style scoped>
.user-info {
  min-width: 650px;
}


.head {
  display: flex;
  justify-content: space-between;
  width: 96%;
  margin-left: 2%;
}

.head .left {
  font-size: 38px;
  font-weight: bold;
  position: relative;
  top: 15px;
}

.head .right {
  height: 30px;
}

.head .right img {
  height: 100%;
}

.content {
  width: 90%;
  margin-top: 20px;
  margin-left: 5%;
}

.title-image {
  height: 160px;
  width: 100%;
  overflow: hidden;
}

.title-image img {
  width: 100%;
}

.title-content {
  background: linear-gradient(30deg, rgb(116, 223, 231), rgb(29, 82, 176)) center;
  padding: 10px 30px;
  display: inline;
  font-size: 26px;
  font-weight: bold;
  color: white;
  margin: auto;
  position: relative;
  top: -25px;
  z-index: 3;
}

.line {
  background: black;
  height: 2px;
}

.introduction {
  padding-left: 100px;
  padding-right: 100px;
  font-size: medium;
  font-weight: bold;
}

.show-info {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.info-content {
  padding: 10px 20px;
  width: auto;
  min-width: 320px;
  height: auto;
  background-color: white;
  border-radius: 1rem;
  box-shadow: 0px 0px 8px 1px #E6E6E6;
}

/* .info-content-info {} */

.company-name {
  cursor: default;
  font-size: 26px;
  font-weight: bold;
  line-height: 60px;
}

.company-name img {
  height: 28px;
  position: relative;
  top: 5px;
}

.sub-info {
  line-height: 40px;
  cursor: default;
  font-size: 20px;
  color: #2c2c2c;
}



.center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.room-number-list {
  max-width: 180px;
  /* 不换行 */
  white-space: nowrap;
  /* 超出部分隐藏 */
  overflow: hidden;
  /* 文本超出时，显示省略标记 */
  text-overflow: ellipsis;
}
</style>