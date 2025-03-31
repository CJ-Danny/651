module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  collectCoverage: true,
  coverageThreshold: {
    global: {
      statements: 0,
      branches: 0,
      functions: 0,
      lines: 0
    }
  },
  coveragePathIgnorePatterns: [
    '/src/$',         
    '/src/router/',   
    '/src/store/'     
  ],
  coverageReporters: ['text-summary', 'html', 'text'],
  collectCoverageFrom: [
    'src/**/*.{js,vue}',
    '!src/main.js',       
    '!**/node_modules/**',
    '!**/coverage/**',
    '!src/router/index.js',  
    '!src/store/index.js'   
  ],
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/src/$1" 
  },
  preset: '@vue/cli-plugin-unit-jest',
  transform: {
    '^.+\\.vue$': 'vue-jest',
    '^.+\\.js$': 'babel-jest',
    '^.+\\axios': 'babel-jest' 
  },
  transformIgnorePatterns: [
    '/node_modules/(?!(axios|element-ui)/)'
  ]
  
  

}