import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/inedx.ts';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import { createPinia } from 'pinia';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import Vue3Lottie from 'vue3-lottie'
const pinia = createPinia();
const app = createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.use(Vue3Lottie);
app.use(router);
app.use(ElementPlus);
app.use(pinia);
app.mount('#app').$nextTick(() => {
  // Use contextBridge
  window.ipcRenderer.on('main-process-message', (_event, message) => {
    console.log(message)
  })
})
