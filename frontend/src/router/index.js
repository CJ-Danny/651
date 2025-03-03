import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '@/store/index' 

let originPush =  VueRouter.prototype.push;  //备份原push方法

VueRouter.prototype.push = function (location, resolve, reject){
    if (resolve && reject) {    //如果传了回调函数，直接使用
        originPush.call(this, location, resolve, reject);
    }else {                     //如果没有传回调函数，手动添加
        originPush.call(this, location, ()=>{}, ()=>{});
    }
}

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/app',
    name: 'app',
    component: () => import('../views/AppView'),

    children: [
      {
        path: 'client/repairment',
        name: 'repairment',
        component: () => import('../views/client/customerRepairList.vue'),
      },
      {
        path: 'client/userinfo',
        name: 'userInfo',
        component: () => import('../views/client/UserInfo.vue'),
      },

      // {
      //   path: 'repairman',
      //   name: 'repairman',
      //   component: () => import('../views/repairman/repair.vue'),
      // },
    ],
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const url = to.name
  // console.log(url)
  // console.log(store.state.userState, store.state.userType)
  if(url === 'login') {
    if(store.state.userState !== -1) {
      next(false)
    } else {
      next()
    }
  } else if(url === 'room' || url === 'statistics' || url === 'peopleManagement' || url === 'repairTopIndex' || url === 'app') {
    // 二级路由守护
    next(false)
  } else if(url === 'rooms' || url === 'repair' || url === 'visitor' || url === 'customerManagement' || url === 'managerManagement' || url === 'maintainerManagement' || url === 'rentRequests' || url === 'roomsDetail') {
    // 管理员界面路由守护
    if(store.state.userState === 1 && store.state.userType === 1) {
      next();
    } else {
      next(false)
    }
  } else if(url === 'repairList') {
    // 维修人员和管理员路由守护
    if(store.state.userState === 1) {
      next();
    } else {
      next(false)
    }
  } else if(url === 'repairment' || url === 'userInfo'){
    // 客户路由守护
    if(store.state.userState === 0) {
      next();
    } else {
      next(false)
    }
  }else {
    // console.log('其它')
    next()
  }
})

export default router
