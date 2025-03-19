<template>
  <div class="info-card">
    <div class="head-bg">
      <img src="@/assets/userInfo/head.jpg" alt="" />
    </div>
    <div style="position: relative;top: -40px;">
      <div class="avatar-border center">
        <div class="avatar"><img src="@/assets/userInfo/avatar.jpg" alt="" /></div>
      </div>
      <div class="name center">{{ name }}</div>
      <div class="sub-name center" style="margin-top: 20px">{{ email }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InfoCard',
  props: {
    name: { type: String, default: 'danny' },
    email: { type: String, default: '1135878957@qq.com' },
  }
}
</script>

<style scoped>
.info-card {
  text-align: center;
  height: 350px;
  width: 250px;
  border-radius: 1rem;
  background-color: #F6FAFF;
  color: black;
  padding: 10px;
  box-shadow: 0px 0px 8px 1px #E6E6E6;
}

.head-bg {
  z-index: 1;
  width: 100%;
  height: 100px;
  overflow: hidden;
  border-radius: .8rem;
}

.head-bg img {
  width: 100%;
}

.avatar-border {
  z-index: 2;
  background-color: rgba(255, 255, 255);
  height: 85px;
  width: 85px;
  border-radius: 50%;
  position: relative;
  left: 83px;
}

.avatar {
  z-index: 3;
  height: 75px;
  width: 75px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
}

.name {
  font-size: 20px;
  font-weight: bold;
}

.sub-name {
  font-size: medium;
  color: rgb(176, 186, 201);
}

.center {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>