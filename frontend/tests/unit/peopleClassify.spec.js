import { shallowMount } from '@vue/test-utils'
import peopleClassify from '@/views/manager/peopleManagement/peopleClassify.vue'

describe('peopleClassify.vue', () => {
  it('Correctly pass navigation data', () => {
    
    const TopIndex2Stub = {
      name: 'TopIndex2',
      template: '<div />',
      props: ['data', 'type']
    }

    const wrapper = shallowMount(peopleClassify, {
      stubs: {
        TopIndex2: TopIndex2Stub
      }
    })
    
    const topIndex = wrapper.findComponent(TopIndex2Stub)
    expect(topIndex.exists()).toBe(true)
    expect(topIndex.props('type')).toBe(1)
    expect(topIndex.props('data')).toEqual(expect.arrayContaining([
      expect.objectContaining({ title: 'Customer' }),
      expect.objectContaining({ title: 'Service Man' })
    ]))
  })
})