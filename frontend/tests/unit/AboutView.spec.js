// tests/views/AboutView.spec.js
import { mount } from '@vue/test-utils'
import AboutView from '@/views/AboutView.vue'

describe('AboutView.vue', () => {
  it('Renders the correct title content', () => {
    const wrapper = mount(AboutView)
    expect(wrapper.find('h1').text()).toMatch('This is an about page')
  })
})