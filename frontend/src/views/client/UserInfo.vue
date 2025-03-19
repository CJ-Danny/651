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
                  <span v-for="(item, i) in roomNumber">
                    <span class="room-number-clickable" @click="showRoomDetails(item)">{{ item }}</span>
                    <span v-show="i !== roomNumber.length - 1">, </span>
                  </span>
                </span>
              </div>
              <h3>Rental History</h3>
              <el-table :data="rentList" stripe style="width: 100%" empty-text="No rental history available">
                
                <el-table-column label="Room No." width="150">
                  <template slot-scope="scope">
                    <div class="room-number-list">
                      <span class="room-number-clickable" @click="showRoomDetails(scope.row.roomNumber)">
                        {{ scope.row.roomNumber }}
                      </span>
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
              </el-table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Room Details Dialog -->
    <el-dialog
      title="Room Details"
      :visible.sync="roomDialogVisible"
      width="30%"
      center
      top="5vh"
      :append-to-body="true"
      :fullscreen="false"
      class="room-details-dialog">
      <div v-if="currentRoomDetails" class="room-details-content">
        <el-descriptions :column="1" border>
          <el-descriptions-item label="Room Number">{{ currentRoomDetails.room.number }}</el-descriptions-item>
          <el-descriptions-item label="Floor">{{ currentRoomDetails.room.floor }}</el-descriptions-item>
          <el-descriptions-item label="Area">{{ currentRoomDetails.room.area }}</el-descriptions-item>
          <el-descriptions-item label="Price">{{ currentRoomDetails.room.price }} CAD/month</el-descriptions-item>
        </el-descriptions>
        
        <div v-if="currentRoomDetails.bills && currentRoomDetails.bills.length > 0">
          <h3 style="margin-top: 20px">Bills</h3>
          <el-table :data="currentRoomDetails.bills" style="width: 100%">
            <el-table-column prop="billId" label="Bill ID" width="80"></el-table-column>
            <el-table-column label="Amount" width="120">
              <template slot-scope="scope">
                {{ scope.row.money }} CAD
              </template>
            </el-table-column>
            <el-table-column label="Due Date">
              <template slot-scope="scope">
                {{ scope.row.due ? scope.row.due.substring(0, 10) : 'N/A' }}
              </template>
            </el-table-column>
            <el-table-column label="Status" width="100" align="center">
              <template slot-scope="scope">
                <el-tag :type="getBillStatusType(scope.row.status)">
                  {{ getBillStatusText(scope.row.status) }}
                </el-tag>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div v-else style="margin-top: 20px; color: #909399;">
          <i class="el-icon-info"></i> No bills available for this room.
        </div>
        
        <div v-if="currentRoomDetails.room.imgUrl" class="room-image-container">
          <img 
            :src="currentRoomDetails.room.imgUrl" 
            alt="Room Image" 
            class="room-image"
          />
        </div>
      </div>
      <div v-else class="text-center">
        <i class="el-icon-loading"></i> Loading room details...
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="roomDialogVisible = false">Close</el-button>
      </span>
    </el-dialog>
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
      // New fields for room details dialog
      roomDialogVisible: false,
      currentRoomDetails: null,
      loadingRoomDetails: false
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
              // Extract room numbers only from approved rentals (status = 1)
              this.roomNumber = res.data.data.rentList
                .filter(rent => rent.status === 1)
                .map(rent => rent.roomNumber);
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
    },
    
    // Methods for bill status display
    getBillStatusType(status) {
      switch (status) {
        case 0:
          return 'warning'; // Unpaid
        case 1:
          return 'success'; // Paid
        default:
          return 'info';
      }
    },
    
    getBillStatusText(status) {
      switch (status) {
        case 0:
          return 'Unpaid';
        case 1:
          return 'Paid';
        default:
          return 'Unknown';
      }
    },
    
    // New method to show room details
    showRoomDetails(roomNumber) {
      this.roomDialogVisible = true;
      this.currentRoomDetails = null;
      
      // Find the rent record that matches this room number
      const rentRecord = this.rentList.find(rent => rent.roomNumber === roomNumber);
      
      if (!rentRecord) {
        this.$message.error('Room information not found');
        this.roomDialogVisible = false;
        return;
      }
      
      // Call API to get room details
      const formData = new FormData();
      formData.append('token', this.$store.state.token);
      formData.append('rentId', rentRecord.rentId);
      
      this.$axios({
        method: 'post',
        url: 'user/getRentInfo',
        data: formData,
      })
        .then((res) => {
          if (res.data.errno === 0 && res.data.data) {
            this.currentRoomDetails = res.data.data;
          } else {
            this.$message.error('Failed to load room details: ' + (res.data.errmsg || 'Unknown error'));
            this.roomDialogVisible = false;
          }
        })
        .catch((err) => {
          console.error('API request failed:', err);
          this.$message.error('Failed to load room details');
          this.roomDialogVisible = false;
        });
    }
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

/* New styles for clickable room numbers */
.room-number-clickable {
  color: #409EFF;
  cursor: pointer;
  text-decoration: underline;
}

.room-number-clickable:hover {
  color: #66b1ff;
}

.text-center {
  text-align: center;
}

.room-image-container {
  margin-top: 20px;
  text-align: center;
  overflow: hidden;
  border-radius: 4px;
  width: 100%;
  /* Create a container with 4:3 aspect ratio */
  position: relative;
  padding-top: 60%; /* 3/4 = 0.75 = 75% for 4:3 ratio */
  /* For 5:3 ratio, use 60% (3/5 = 0.6 = 60%) */
  /* padding-top: 60%; */
}

.room-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 4px;
}

/* Dialog styles */
.room-details-dialog .el-dialog {
  max-height: 90vh;
  display: flex;
  flex-direction: column;
}

.room-details-dialog .el-dialog__body {
  overflow-y: auto;
  padding: 15px 20px;
}

.room-details-content {
  overflow-y: auto;
}
</style>