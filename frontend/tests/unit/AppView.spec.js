// AppView.spec.js
import { createLocalVue, mount } from '@vue/test-utils'
import ElementUI from 'element-ui'
import AppView from '@/views/AppView.vue'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(ElementUI)
localVue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user: {
      state: -1, 
      type: 'guest' 
    }
  }
})

describe('AppView.vue', () => {
  it('Render child components correctly', () => {
    const wrapper = mount(AppView, {
      localVue,
      store, 
      stubs: ['router-view', 'SideIndex'] 
    })
    expect(wrapper.find('.rightContainer').exists()).toBe(true)
  })
})