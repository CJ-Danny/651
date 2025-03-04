<template>
  <TopIndex2 :data="dt" :type="3"></TopIndex2>
</template>

<script>
import TopIndex2 from "@/components/TopIndex2";
export default {
  name: "repairTop",
  components: { TopIndex2 },
  data() {
    return {
      dt: [
        {src: require('@/assets/管理员端/statistics/icon0.png'), title: 'New Rent Appliaction'},
        {src: require('@/assets/管理员端/statistics/icon1.png'), title: 'Processed Rent Application'}
      ],
    }
  },
}
</script>
<style scoped>
</style>
