import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '@/store/index' 

let originPush =  VueRouter.prototype.push;  

VueRouter.prototype.push = function (location, resolve, reject){
    if (resolve && reject) {    
        originPush.call(this, location, resolve, reject);
    }else {                     
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
        path: 'manager/people',
        name: 'peopleManagement',
        component: () => import('../views/manager/peopleManagement/peopleClassify'),
        children: [
          {
            path: 'customer',
            name: 'customerManagement',
            component: () => import('../views/manager/peopleManagement/customerInfo'),
          },
          {
            path: 'maintainer',
            name: 'maintainerManagement',
            component: () => import('../views/manager/peopleManagement/maintainerInfo'),
          },
        ],
      },

      {
        path: 'manager/apply',
        name: 'applyTopIndex',
        component: () => import('../views/manager/apply/applyTop.vue'),
        children: [
          {
            path: 'applyList',
            name: 'applyList',
            component: () => import('../views/manager/apply/apply.vue'),
          },
        ],
      },
      {
        path:'manager/knowledge',
        name:'knowledgeManager',
        component: () => import('../views/manager/repairment/knowledge'),

      },
      {
        path:'manager/room',
        name:'roommanagement',
        component: () => import('../views/manager/room/RoomDiagram2.vue'),

      },
      {
        path: 'manager/repair',
        name: 'repairTopIndex',
        component: () => import('../views/manager/repairment/repairTop'),
        children: [
          {
            path: 'repairlist',
            name: 'repairList',
            component: () => import('../views/manager/repairment/repairment.vue'),
          },
        ],
      },{
        path: 'manager/repair/knowledge',
        name: 'knowledge',
        component: () => import('../views/manager/repairment/knowledge'),
        children: [
          {
            path: 'repairlist',
            name: 'repairList2',
            component: () => import('../views/manager/repairment/repairment.vue'),
          },
        ],
      },
      {
        path: 'client/room',
        name: 'clientRoom',
        component: () => import('../views/client/RoomDiagram.vue') 
      },
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
  
  const isLoggedIn = store.state.userState !== -1; 
  const isAdmin = store.state.userState === 1;
  const isUser = store.state.userState === 0;

  
  if (to.name === 'login' && isLoggedIn) {
    next({ name: 'home' });
    return;
  }

 
  if (to.path.startsWith('/app/manager')) {
    if (isAdmin) {
      next(); 
    } else {
      next(false); 
      
      
    }
    return;
  }

  
  if (to.path.startsWith('/app/client')) {
    if (isUser) {
      next(); 
    } else {
      next(false); 
    }
    return;
  }

  
  next();
});

export default router
