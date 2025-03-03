import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import * as echarts from 'echarts';
import axios from 'axios';
import locale from 'element-ui/lib/locale/lang/en'

Vue.use(ElementUI, { locale })

Vue.config.productionTip = false

Vue.use(ElementUI);

Vue.prototype.$axios = axios;
Vue.prototype.$echarts = echarts;

axios.defaults.baseURL = 'http://15.157.62.32:8000/api/';

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
