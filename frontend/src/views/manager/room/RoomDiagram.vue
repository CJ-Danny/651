<template>
  <el-container style="width: 100%; height: 85%;" class="main">

    
    <el-aside style="flex: 1; min-width: 0" v-loading="isLoading" class="left detail-info-card">
 
  <el-container 
    v-for="floorInfo in floorRoomMap" 
    :key="floorInfo.floor" 
    class="floor-card"
  >
    <el-aside width="10%" class="floor-label"> Floor {{ floorInfo.floor }} </el-aside>
    <el-main style="line-height: 0; padding: 0">
      
      <div 
        class="rooms" 
        v-for="line in [1, 2, 3]" 
        :key="line"
      >
       
        <div
        v-for="(roomIdx, i) in getRoomIdxListByLine(floorInfo.roomIdxList, line)"
  :key="roomList[roomIdx].roomId || i" 
  style="display: flex; align-items: center; position: relative" 
>
          <el-tooltip
            effect="light"
            placement="bottom"
            transition="none"
            :disabled="isMultiRenting && roomList[roomIdx].status !== 0"
            @mouseleave.native="removeAllTooltip"
          >
            <template slot="content">
              <div style="font-size: 14px; font-weight: bold">
                <div v-if="roomList[roomIdx].status === 0" style="color: #67c23a">Not leased</div>
                <div v-else-if="roomList[roomIdx].status === 1" style="color: #ffa034">Under lease</div>
                <div v-else-if="roomList[roomIdx].status === 2" style="color: #e03d5e">Property fees unpaid</div>
                <div v-else-if="roomList[roomIdx].status === 3" style="color: #7ccafb">Under repair</div>
                <div v-else-if="roomList[roomIdx].status === 23">
                  <span style="color: #e03d5e">Property fees unpaid</span>
                  <span style="color: #7ccafb"> Under repair</span>
                </div>
                <div v-else style="color: #6e6e6e">Not available</div>
              </div>

              <div style="font-size: 14px">
                {{ floorInfo.floor }} floor · {{ roomList[roomIdx].roomNumber }} ·
                {{ roomList[roomIdx].roomName }}
              </div>
              <div>area: {{ roomList[roomIdx].area }} </div>
              <div>fees: {{ roomList[roomIdx].price }} CAD/month</div>
            </template>
            <div :style="roomCardStyle(roomIdx)" @click="selectRoom($event, roomIdx)" class="room-card">
              {{ roomList[roomIdx].roomNumber }}
            </div>
          </el-tooltip>
          <div v-if="line === 2 && i === 0">
            <img src="@/assets/roomInfo/mid.png" style="width: 695px; height: 100px; margin-right: 5px" />
          </div>
        </div>
      </div>
    </el-main>
  </el-container>
</el-aside>

   
    <el-main class="right">
      
      <div class="detail-info-card">
       
        <div v-if="!isMultiRenting">
          <div class="legend">
            <span class="legend-icon" style="background: #eee"></span><span>Not leased</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #ffa034"></span><span>Under lease</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #e03d5e"></span><span>Under lease, Property fees unpaid</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #7ccafb"></span><span>Under lease, Under repair</span>
          </div>
        </div>
        <div v-else>
          <div class="legend">
            <span class="legend-icon" style="background: #eee"></span><span>Not leased</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #67c23a"></span><span>Chosed</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #f3d19e"></span><span>Under lease</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #d77689"></span><span>Under lease, Property fees unpaid</span>
          </div>
          <div class="legend">
            <span class="legend-icon" style="background: #a8deff"></span><span>Under lease, Under repair</span>
          </div>
        </div>
      </div>

    
<div class="detail-info-card multi-rent-card">
  <div style="align-self: center; width: 100%">
    <div v-if="!isMultiRenting">
      <el-button type="success" @click="startMultiRent">View Details</el-button>
    </div>
    <div v-else>
      <el-button @click="cancelMultiRent">Cancel</el-button>
      <el-button type="primary" @click="confirmMultiRent" :disabled="selectedCount === 0">
        Confirm
      </el-button>
    </div>
  </div>
  <div v-if="isMultiRenting">
    <div style="font-weight: bold; margin-top: 5px">
      <span> Choose {{ selectedCount }} rooms </span>
      <span>
        <el-button
          type="info"
          size="mini"
          style="margin-left: 10px"
          v-if="selectedCount > 0"
          @click="clearSelect"
        >
          clear all
        </el-button>
      </span>
    </div>
   
    <div 
      v-for="room in roomList.filter((_, i) => isRoomSelected[i])" 
      :key="room.roomId || room.roomNumber" 
      style="margin-left: 5px"
    >
      {{ room.floor }} floor · {{ room.roomNumber }} · {{ room.roomName }}
    </div>
  </div>
</div>
      
      <div class="detail-info-card" v-if="selectedRoom !== null && !isMultiRenting">
        <img :src="selectedRoom.localImg" style="width: 90%; height: 110px" />
        <br />
        <div v-if="rentLoading" class="loading-container">
    <i class="el-icon-loading"></i> 
    
  </div>

  <div v-else>

  </div>
        <div style="font-size: 18px; font-weight: bold">
          <div v-if="selectedRoom.status === 0" style="color: #67c23a">Not leased</div>
          <div v-else-if="selectedRoom.status === 1" style="color: #ffa034">Under lease</div>
          <div v-else-if="selectedRoom.status === 2" style="color: #e03d5e">Property fees unpaid</div>
          <div v-else-if="selectedRoom.status === 3" style="color: #7ccafb">Under repair</div>
          <div v-else-if="selectedRoom.status === 23">
            <span style="color: #e03d5e">Property fees unpaid</span>
            <span style="color: #7ccafb"> Under repair</span>
          </div>
          <div v-else style="color: #6e6e6e">Not available</div>
        </div>
        <div>
          <span class="el-icon-s-data" style="margin-right: 15px"></span>
          <span>Floor {{ selectedRoom.floor }} · Room {{ selectedRoom.roomNumber }} </span>
        </div>
        <div>
          <span class="el-icon-s-home" style="margin-right: 15px"></span>
          <span>Area: {{ selectedRoom.area }} </span>
        </div>
        <div>
          <span class="el-icon-s-order" style="margin-right: 15px"></span>
          <span>Fees: {{ selectedRoom.price }} CAD/Month</span>
        </div>
        <div v-if="selectedRoom.status !== 0">
          <div>
            <span class="el-icon-s-custom" style="margin-right: 15px"></span>
            <span>Renter: {{ selectedRoom.trueName }}</span>
          </div>
          <div>
            <span class="el-icon-s-flag" style="margin-right: 15px"></span>
            <span
              >Rental Duration: <br />
              {{ selectedRoom.startTime.substring(0, 10) }} - {{ selectedRoom.endTime.substring(0, 10) }}
            </span>
          </div>
        </div>
        <div v-if="selectedRoom.status === 3 || selectedRoom.status === 23">
          <el-button
            style="background: #7ccafb; color: white"
            @click="$router.push('/app/manager/repair/repairlist?type=0')"
            size="small"
          >
            Watch RepairList
          </el-button>
        </div>
      </div>
    </el-main>
    <RentRoomDialog ref="rentRoomDialogRef"></RentRoomDialog>
    <RentRoomDialog ref="rentDialog" @payment-success="loadRooms" />
  </el-container>
</template>

<script>
  import RentRoomDialog from './components/RentRoomDialog.vue';
  import img1 from '@/assets/room-images/room1.jpg'
import img2 from '@/assets/room-images/room2.jpg'
import img3 from '@/assets/room-images/room3.jpg'
import img4 from '@/assets/room-images/room4.jpg'
import img5 from '@/assets/room-images/room5.jpg'
  export default {
    components: { RentRoomDialog },
    data() {
      return {
        localRoomImages: [img1, img2, img3, img4, img5],
        roomList: [],
        rentLoading: false,
        floorRoomMap: [],

        isMultiRenting: false,
        isRoomSelected: [],
        selectedCount: 0,

        selectedRoom: null,

        isLoading: true,
        doUpdate: 0,
      };
    },
    methods: {
      async loadRooms() {
    try {
      const res = await this.$axios.post('/room/getRoomsInfo', {});
      this.roomList = res.data.data.map(room => ({
        ...room,
        rentID: room.rentID
      }));
      this.updateRoomStatus(); 
    } catch (err) {
      console.error('load failed:', err);
    }
  },
  updateRoomStatus() {
    
    this.roomList.forEach(room => {
      const relatedBills = this.$refs.rentDialog.bills.filter(
        bill => bill.rentID === room.rentID
      );
      
      const allPaid = relatedBills.every(bill => bill.status === 1);
      if (allPaid) room.status = 1; 
    });
  },

      
      startMultiRent() {
        this.isMultiRenting = true;
        this.isRoomSelected.fill(false);
        this.selectedCount = 0;
      },
      clearSelect() {
        this.isRoomSelected.fill(false);
        this.selectedCount = 0;
        this.isMultiRenting = false;
        this.isMultiRenting = true;
      },
      cancelMultiRent() {
        this.isMultiRenting = false;
      },
      confirmMultiRent() {
        let selectedRoomList = [];
        for (let i = 0; i < this.isRoomSelected.length; i++) {
          if (this.isRoomSelected[i]) {
            selectedRoomList.push(this.roomList[i]);
          }
        }
        this.$refs.rentRoomDialogRef.show(selectedRoomList);
      },
      async selectRoom($event, roomIdx) {
  if (!this.isMultiRenting) {
    try {
          this.rentLoading = true;
          
         
          const randomIndex = Math.floor(Math.random() * this.localRoomImages.length);
          const selectedImg = this.localRoomImages[randomIndex];

          this.selectedRoom = {
            ...this.roomList[roomIdx],
            localImg: selectedImg, 
            price: this.roomList[roomIdx].price
          };
        } finally {
          this.rentLoading = false;
        }
      } 
    else{
    if (this.roomList[roomIdx].status !== 0 && this.roomList[roomIdx].status !== 1 && this.roomList[roomIdx].status !== 2 && this.roomList[roomIdx].status !== 3 && this.roomList[roomIdx].status !== 23) return;
    this.selectedRoom = this.roomList[roomIdx];
    if (this.isRoomSelected[roomIdx]) this.selectedCount--;
    else this.selectedCount++;
    this.isRoomSelected[roomIdx] = !this.isRoomSelected[roomIdx];
    this.doUpdate++;}
  
},
      blurRoom() {
        this.selectedRoom = null;
      },
      removeAllTooltip() {
        document.querySelectorAll('.el-tooltip__popper').forEach((el) => el.remove());
      },
      getRoomIdxListByLine(list, line) {
        if (line === 1) return list.slice(0, 9);
        else if (line === 2) return list.slice(9, 11);
        else if (line === 3) return list.slice(11, 20);
      },
    },
    mounted() {
  this.$axios
    .post('/room/getRoomsInfo', {})
    .then((res) => {
      
      this.roomList = res.data.data.map(room => ({
        ...room, 
        rentID: room.rentID || null 
      }));

      
      console.log('room data:', this.roomList);

     
      this.isRoomSelected = Array(this.roomList.length).fill(false);
      var floorList = [
        ...new Set(
          this.roomList
            .filter((room) => 'floor' in room)
            .map((room) => room.floor)
            .filter((floor) => floor !== null)
        ),
      ].sort((r1, r2) => Number.parseInt(r1) - Number.parseInt(r2));

      this.floorRoomMap = floorList.map((floor) => {
        var idxList = [];
        for (let i = 0; i < this.roomList.length; i++) {
          const room = this.roomList[i];
          if (room.floor === floor) {
            idxList.push(i);
          }
        }
        return {
          floor: floor,
          roomIdxList: idxList,
        };
      });

      this.isLoading = false;
    })
    .catch((err) => {
      console.error('load failed:', err);
      this.$message.error('unable to load');
    });
},
    computed: {
      roomCardStyle() {
        return (roomIdx) => {
          const room = this.roomList[roomIdx];

          let color = '#909399';
          if (!this.isMultiRenting) {
            if (room.status === 0) color = '#eee';
            else if (room.status === 1) color = '#ffa034';
            else if (room.status === 2) color = '#e03d5e';
            else if (room.status === 3) color = '#7ccafb';
            else if (room.status === 23)
              color = 'repeating-linear-gradient(45deg, #e03d5e, #e03d5e 15px, #7ccafb 0px, #7ccafb 30px)';
          } else {
            if (room.status === 0) color = this.isRoomSelected[roomIdx] ? '#67C23A' : '#eee';
            else if (room.status === 1) color = '#f3d19e';
            else if (room.status === 2) color = '#d77689';
            else if (room.status === 3) color = '#a8deff';
            else if (room.status === 23)
              color = 'repeating-linear-gradient(45deg, #d77689, #d77689 15px, #a8deff 0px, #a8deff 30px)';
          }

          let fontColor = '';
          if (color === '#eee') fontColor = 'black';
          else fontColor = 'white';

          let cursor = 'pointer';
          if (this.isMultiRenting && ![0, 1,2,3,23].includes(room.status)) cursor = 'not-allowed';

          const baseWidth = 40;
          let width = 0;
          let margin = 5;

          if (room.area <= 50) width = baseWidth;
          else if (room.area <= 100) width = baseWidth * 1.5 + margin * 0.5;
          else if (room.area <= 200) width = baseWidth * 2 + margin;
          else width = baseWidth * 2 + margin * 2;

          return {
            '--background': color,
            '--color': fontColor,
            '--width': width + 'px',
            '--margin': margin + 'px',
            '--cursor': cursor,
            '--doUpdate': this.doUpdate,
          };
        };
      },
    },
  };
</script>

<style scoped>
  .main {
    margin: 0 20px 20px 20px;
  }

  .left {
    min-height: 100vh;
  }

  .floor-card {
  padding: 10px;
  min-height: 160px;
  position: relative;
  display: flex;
  border-bottom: 20px dotted #e7e7e7;
  flex: 1;  
}

  .floor-label {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-right: 20px;
    font-size: 18px;
  }

  .rooms {
  display: flex;
  padding: 0;
  gap: 5px;  
  flex-wrap: wrap;
}

  .room-card {
    position: relative;
    width: var(--width);
    height: 110px;
    border-radius: 30px;
    margin: 0px var(--margin) var(--margin) 0px;
    background: var(--background);
    color: var(--color);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: var(--cursor);
  }

  .room-card:hover {
    box-sizing: border-box;
    border: solid #00000040 5px;
  }

  .right {
    position: fixed;
    float: right;
    width: 25%;
    right: 50px;
  }

  .detail-info-card {
    max-width: 100%;
    margin: 5px;
    background: white;
    border-radius: 5px;
    padding: 15px;
    display: flex;
    flex-direction: column;
    box-shadow: 10px 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
  .multi-rent-card {
    max-height: 55vh;
    overflow-y: auto;
  }

  .legend {
    margin-bottom: 5px;
    display: flex;
    align-items: center;
  }

  .legend-icon {
    width: 20px;
    height: 20px;
    border-radius: 25%;
    margin-right: 6px;
    display: inline-block;
  }
  
  @media screen and (max-width: 1600px) {
  .mid-image {
    width: 100% !important;  
    height: 40px !important;
  }}
</style>
