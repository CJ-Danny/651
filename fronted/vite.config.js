import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // 让应用可通过外部访问
    port: 8080,       // 可以根据需要修改端口
  }
})
