<template>
  <TopIndex2 :data="dt" :type="4"></TopIndex2>
</template>

<script>
import TopIndex2 from "@/components/TopIndex2";
export default {
  name: "repairTop",
  components: { TopIndex2 },
  data() {
    return {
      dt: [
        {src: require('@/assets/管理员端/statistics/icon0.png'), title: 'Pending maintenance orders'},
        {src: require('@/assets/管理员端/statistics/icon1.png'), title: 'Completed maintenance orders'}
      ],
    }
  },
}
</script>
<style scoped>
</style>
