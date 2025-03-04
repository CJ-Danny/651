<template>
  <div style="margin-left: 6vw;margin-top:30px">
    <div style="display: flex">
      <div style="background-color: #FBFBFB;width:35vw;height:50px;display: flex;align-items: center">
        <div style="background-color: #0d9fda;width:10px;height:50px"></div>
        <div style="padding-left: 25px">Welcome</div>
      </div>

    </div>
    <div style="float:right;margin-right: 50px;margin-top: -70px"><img src="../../../assets/repair/logo.png"></div>

    <div>
      <div>
        <el-table
            :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 95%"
            v-loading="isLoading"
            >
          <el-table-column
            prop="rentId"
              label="Rent id" align="center"
              width="100"
              sortable>
          </el-table-column>

          <el-table-column
              prop="userId"
              label="User id" align="center"
              width="100"
              sortable>
          </el-table-column>

          <el-table-column
              prop="roomId"
              label="RoomID"
              width="100"
              align="center"
          >
          </el-table-column>

          <el-table-column
              prop="applyTime"
              label="Apply Time"
              min-width="8"
              align="center"
          >
            <template slot-scope="scope">{{ formatDate(scope.row.applyTime, "applyTime" ) }}</template>
          </el-table-column>

          <el-table-column
              prop="startTime"
              label="Start Time"
              width="120"
              align="center"
          >
            <template slot-scope="scope">{{ formatDate(scope.row.startTime, "startTime" ) }}</template>
          </el-table-column>

          <el-table-column

              prop="endTime"
              label="End Time"
              width="120"
              align="center"
          >
            <template slot-scope="scope">{{ formatDate(scope.row.endTime, "endTime" ) }}</template>
          </el-table-column>

          <el-table-column
              prop="status"
              label="Status"
              width="140"
              align="center"
          >
          </el-table-column>

          <el-table-column
              v-if="$route.query.type==='0'"
              label="Operation"
              width="180"
              align="center"
          >
            <template slot-scope="scope">
              <el-button type="success" @click="openDialog(scope.row, 1)">Approve</el-button>
              <el-button type="danger" @click="openDialog(scope.row, 2)">Reject</el-button>
            </template>
          </el-table-column>
        </el-table>

        <el-dialog :visible.sync="dialogVisible" title="Confirm Action">
          <p>Are you sure you want to {{ actionType === 1 ? 'approve' : 'reject' }} this application?</p>
          <span slot="footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button type="primary" @click="reviewRent">Confirm</el-button>
          </span>
        </el-dialog>


        <div class="pageDiv">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[5, 10, 15, 20]"
              :page-size="10"
              layout="total, sizes, prev, pager, next, jumper"
              :total="this.tableData.length">
          </el-pagination>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "apply",

  data() {
    return {
      isLoading:true,
      dialogFormVis2: false,
      dialogVisible: false,
      currentPage: 1,
      pageSize: 10,
      tableData: [],
      formLabelWidth: '120px',
    }
  },

  created() {
    this.createView(this.$route.query.type || 0);
  },


  watch: {
    '$route.query.type': {
      handler(newVal) {
        this.tableData=[];
        this.isLoading=true;
        this.createView(this.$route.query.type)
      },
      deep: true
    }
  },

  methods: {
    formatDate(dateString, type) {
      if (!dateString) return "";
      // Convert to Date object
      const date = new Date(dateString);
      // Format based on type
      if (type === "startTime" || type === "endTime") {
        return date.toISOString().split("T")[0]; // Keep only YYYY-MM-DD
      } else if (type === "applyTime") {
        return date.toISOString().replace("T", " ").split(".")[0]; // Keep YYYY-MM-DD HH:mm:ss
    }
    
    return dateString; // Fallback if type is unknown
    },

    openDialog(row, action) {
      this.selectedRent = row;
      this.actionType = action;
      this.dialogVisible = true;
    },
    reviewRent() {
    const formData = new FormData();
    formData.append("rentId", this.selectedRent.rentId);
    formData.append("status", this.actionType);

    this.$axios.post('/manager/reviewRent', formData)
      .then(() => {
        this.$message.success(this.actionType === 1 ? 'Approved' : 'Rejected');
        this.dialogVisible = false;
        this.createView(this.$route.query.type || 0);
      })
      .catch(() => this.$message.error('Action failed'));
    },

    handleSizeChange(val) {
      this.pageSize = val;
      console.log(this.pageSize);
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      console.log(this.currentPage);
    },
    createView(type) {
      const formData = new FormData()
      formData.append("status", type);
      if (type == 0){
        this.$axios({
          method: 'post',
          url: '/manager/getRentInfo',
          data: formData
        })
            .then((res) => {
              if (res.data.errno === 0) {
                this.tableData=res.data.data;
                this.isLoading=false;
              } else {
                console.log(res.data);
              }
            })
            .catch((err) => {
              console.log(err);
            });
      } else {
              const formData1 = new FormData();
              formData1.append("status", "1");  // Approved
              const formData2 = new FormData();
              formData2.append("status", "2");  // Rejected

              Promise.all([
                this.$axios.post('/manager/getRentInfo', formData1),
                this.$axios.post('/manager/getRentInfo', formData2)
              ]).then(([res1, res2]) => {
                if (res1.data.errno === 0 && res2.data.errno === 0) {
                  this.tableData = [...res1.data.data, ...res2.data.data];  // Combine results
                }
                this.isLoading = false;
              }).catch((err) => console.log(err));
            }
          }
  }
}
</script>

<style scoped>
.pageDiv {
  padding-top: 30px;
  text-align: center;
  padding-bottom: 50px;
}
</style>

<style>
.el-table .warning-row {
    background: rgba(245,108,108, 0.12);
}

.el-table .strike-row {
    background: rgb(250,250,250);
}
</style>
