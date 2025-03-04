<template>
  <TopIndex2 :data="dt" :type="1"></TopIndex2>
</template>

<script>
import TopIndex2 from "@/components/TopIndex2";
export default {
  name: "Data",
  components: {TopIndex2},
  data() {
    return {
      dt: [
        {src: require('@/assets/peopleManagement/客户管理.png'), title: 'Customer'},
        {src: require('@/assets/peopleManagement/管理员信息.png'), title: 'Manager'},
        {src: require('@/assets/peopleManagement/维修人员信息.png'), title: 'Service Man'}
      ],
    }
  },
}
</script>
<style scoped>
</style>
