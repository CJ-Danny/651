module.exports = {
    preset: 'jest-preset-vue',
    transform: {
        '^.+\\.vue$': 'vue-jest',
        '^.+\\.js$': 'babel-jest'
    },
    testEnvironment: 'jsdom',
    moduleFileExtensions: ['js', 'vue', 'json'],
}
