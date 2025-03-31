import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    userState: -1,  //区分用户/管理员 用户：0 管理员：1
    userType: -1,   //区分具体类型
    adminID: -1,
  },
  getters: {
  },
  mutations: {
    set_token(state, token) {
      state.token = token;
    },
    set_userState(state, s) {
      state.userState = s;
    },
    set_userType(state, type) {
      state.userType = type;
    },
    set_adminID(state, id) {
      state.adminID = id;
    }
  },
  actions: {
  },
  modules: {
  },
  plugins: [
    createPersistedState({
      storage: window.localStorage,
      key: 'store',
      render(state) {
        return { ...state };
      },
    }),
  ],
})
