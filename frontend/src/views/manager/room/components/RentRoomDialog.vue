<template>
  <el-dialog 
    :visible.sync="visible" 
    title="Bill Management" 
    width="50%"
    height="100%"
    @closed="handleClose"
  >
  
    <el-card class="box-card" v-loading="billLoading">
      <div slot="header">Historical Bills</div>
      <el-table :data="bills" style="width: 100%">
        <el-table-column prop="billId" label="ID" width="80"></el-table-column>
        <el-table-column label="Status" width="120">
          <template slot-scope="scope">
            <el-tag :type="scope.row.status | statusTypeFilter">
              {{ scope.row.status | statusTextFilter }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="money" label="Amount" width="120">
          <template slot-scope="scope">${{ scope.row.money }}</template>
        </el-table-column>
        
        <el-table-column label="Created" width="180">
  <template slot-scope="scope">
    {{ formatDate(scope.row.createTime) }} 
  </template>
</el-table-column>
        
        <el-table-column label="Operations" width="120">
          <template slot-scope="scope">
            <el-button 
              v-if="scope.row.status === 0"
              type="text" 
              @click="handlePay(scope.row.billId)"
            >Pay</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

   

<el-table-column label="Due Date" width="180">
  <template slot-scope="scope">
    {{ formatDate(scope.row.due) }} 
  </template>
</el-table-column>
    <el-card class="box-card" style="margin-top: 20px;">
      <div slot="header">Create New Bill</div>
      <el-form :model="newBill" :rules="rules" ref="billForm">
        <el-form-item label="Due Date" prop="due">
          <el-date-picker
            v-model="newBill.due"
            type="date"
            placeholder="Select due date"
            value-format="yyyy-MM-dd"
          ></el-date-picker>
        </el-form-item>
        
        <el-form-item label="Amount" prop="money">
          <el-input-number 
            v-model="newBill.money" 
            :min="1" 
            :precision="2"
            controls-position="right"
          ></el-input-number>
        </el-form-item>

        <el-button type="primary" @click="handleCreate">Create Bill</el-button>
      </el-form>
    </el-card>
  </el-dialog>
</template>

<script>
export default {
  filters: {
    statusTypeFilter(status) {
      return status === 1 ? 'success' : 'danger'
    },
    statusTextFilter(status) {
      return status === 1 ? 'Paid' : 'Unpaid'
    }
  },

  data() {
    return {
      visible: false,
      bills: [],
      billLoading: false,
      currentRentId: null,
      newBill: {
        due: '',
        money: 0
      },
      rules: {
        due: [
          { required: true, message: 'Please select due date', trigger: 'blur' }
        ],
        money: [
          { required: true, message: 'Please input amount', trigger: 'blur' }
        ]
      }
    }
  },

  methods: 
  
  {
    formatDate(isoString) {
  if (!isoString) return 'N/A'; 
  try {
    const date = new Date(isoString);
    const year = date.getFullYear(); 
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0'); 
    return `${year}-${month}-${day}`; 
  } catch (error) {
    console.error('failed:', isoString);
    return 'Invalid Date';
  }
},
  show(rooms) {
    if (rooms.length === 0 || !rooms[0].rentID) {
      this.$message.error('Please select exactly one room');
      return;
    }

   
    
    
    this.currentRentId = rooms[0].rentID; 
    this.loadBills();
    this.visible = true;
  },

    async loadBills() {
      try {
    this.billLoading = true;
    const formData = new FormData();
    formData.append('rentID', this.currentRentId); 
    const res = await this.$axios.post(
      '/room/getBills',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data' 
        }
      }
    );
        
        if (res.data.errno === 0) {
          
        this.bills = res.data.bills; 
      
      }
      } catch (error) {
        this.$message.error('Failed to load bills')
      } finally {
        this.billLoading = false
      }
    },

    async handleCreate() {
  try {
    await this.$refs.billForm.validate();

    const formData = new FormData();
    formData.append('rentID', this.currentRentId);
    formData.append('due', this.newBill.due);
    formData.append('money', this.newBill.money);

    
    
    const res = await this.$axios.post('/room/createBill', 
    formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data' 
        }
      });

    console.log('Create response:', res.data);

    if (res.data.errno === 0) {
      
      this.$message.success('successfully created');
      
      await this.loadBills(); 
      this.resetForm();
    }
  } catch (error) {
    console.error('Create error:', error);
    this.$message.error(error.response?.data?.msg || 'Create bill failed');
  }
},

async handlePay(billId) {
  try {
    const formData = new FormData();
    formData.append('billID', billId);
    formData.append('status', 1);
    const res = await this.$axios.post('/room/payBill', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });

    if (res.data.errno === 0) {
      this.$message.success('Payment successful');
      await this.loadBills(); 
      this.$emit('payment-success'); 
    }
  } catch (error) {
    this.$message.error('Payment failed');
  }
},

    resetForm() {
      this.newBill = {
        due: '',
        money: 0
      }
    },

    handleClose() {
      this.$refs.billForm.resetFields()
      this.bills = []
      this.currentRentId = null
    }
  }
}
</script>

<style scoped>
.box-card {
  margin-bottom: 20px;
}
.el-date-editor.el-input {
  width: 100%;
}
.el-input-number {
  width: 200px;
}
</style>