module.exports = {
  "*.{js,vue}": [
    "vue-cli-service lint",  
    "npm run test:unit -- --findRelatedTests" 
  ]
}