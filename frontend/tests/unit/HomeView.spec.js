import { createLocalVue, mount } from '@vue/test-utils'
import Vuex from 'vuex'
import HomeView from '@/views/HomeView.vue'

const localVue = createLocalVue()
localVue.use(Vuex)

describe('HomeView.vue', () => {
  let store
  beforeEach(() => {
    store = new Vuex.Store({
      state: {
        userState: -1,
        userType: null,
        user: { 
            state: -1, 
            type: null 
          }
      }
    })
  });
  document.body.innerHTML = `
  <div id="box"></div>
`;
  it('Display main title correctly', () => {
    const wrapper = mount(HomeView, {
      localVue,
      store
    })
    expect(wrapper.find('.property-title').exists()).toBe(true)
  })
})