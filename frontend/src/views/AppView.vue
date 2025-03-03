<template>
  <div class="AppView">
    <div class="container">
      <SideIndex></SideIndex>

      <div class="rightContainer">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import SideIndex from "@/components/sideIndex/SideIndex.vue";
export default {
  name: "AppView",
  components: { SideIndex },
  data() {
    return {

    }
  },

}
</script>

<style scoped>
.AppView {
  width: 100vw;
  height: 100vh;
  background-color: #21232F;
  /* overflow: hidden; */
}

.container {
  margin-left: 0;
  margin-right: 0.6vw;
  padding: 0;
  min-width: 99%;
  /* overflow: hidden; */
}

.rightContainer {
  margin-left: 90px;
  margin-top: 2vh;
  height: 96vh;
  width: fill;
  background-color: rgb(244, 247, 254);
  display: inline-block;
  overflow-y: scroll;
  overflow-x: hidden;
  scrollbar-width: thin;
  scrollbar-color: #78AAF0 #F9F9F9;
}

.rightContainer::-webkit-scrollbar {
  width: 10px;
}

.rightContainer::-webkit-scrollbar-thumb {
  background-color: #78AAF0;
}

</style>
