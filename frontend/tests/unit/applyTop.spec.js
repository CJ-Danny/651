import { shallowMount } from '@vue/test-utils'
import applyTop from '@/views/manager/apply/applyTop.vue'

describe('applyTop.vue', () => {
  it('Correctly render the top navigation component', () => {
    
    const TopIndex2Stub = {
      name: 'TopIndex2',
      template: '<div />',
      props: ['data', 'type']
    }

    const wrapper = shallowMount(applyTop, {
      stubs: {
        TopIndex2: TopIndex2Stub
      }
    })
    
    const topIndex = wrapper.findComponent(TopIndex2Stub)
    expect(topIndex.exists()).toBe(true)
    expect(wrapper.vm.dt).toHaveLength(2)
    expect(wrapper.vm.dt[0].title).toBe('New Rent Appliaction')
  })
})