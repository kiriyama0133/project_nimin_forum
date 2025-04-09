import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/inedx.ts';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import { createPinia } from 'pinia';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import Vue3Lottie from 'vue3-lottie'
import ToastService from 'primevue/toastservice';
const pinia = createPinia();
const app = createApp(App);
import PrimeVue from 'primevue/config';
import { definePreset } from '@primeuix/themes';
import Aura from '@primeuix/themes/aura';
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

const Noir = definePreset(Aura, {
  semantic: {
      primary: {
          50: '{zinc.50}',
          100: '{zinc.100}',
          200: '{zinc.200}',
          300: '{zinc.300}',
          400: '{zinc.400}',
          500: '{zinc.500}',
          600: '{zinc.600}',
          700: '{zinc.700}',
          800: '{zinc.800}',
          900: '{zinc.900}',
          950: '{zinc.950}'
      },
      colorScheme: {
          light: {
              primary: {
                  color: '{zinc.950}',
                  inverseColor: '#ffffff',
                  hoverColor: '{zinc.900}',
                  activeColor: '{zinc.800}'
              },
              highlight: {
                  background: '{zinc.950}',
                  focusBackground: '{zinc.700}',
                  color: '#ffffff',
                  focusColor: '#ffffff'
              }
          },
          dark: {
              primary: {
                  color: '{zinc.50}',
                  inverseColor: '{zinc.950}',
                  hoverColor: '{zinc.100}',
                  activeColor: '{zinc.200}'
              },
              highlight: {
                  background: 'rgba(250, 250, 250, .16)',
                  focusBackground: 'rgba(250, 250, 250, .24)',
                  color: 'rgba(255,255,255,.87)',
                  focusColor: 'rgba(255,255,255,.87)'
              }
          }
      }
  }
});

app.use(PrimeVue, {
  theme: {
      preset: Noir,
      options: {
        prefix: 'p',
        darkModeSelector: '.darkmode',
        cssLayer: false
    }
  }
});
app.use(PrimeVue);
app.use(Vue3Lottie);
app.use(router);
app.use(ElementPlus);
app.use(pinia);
app.use(ToastService);
app.mount('#app').$nextTick(() => {
  // Use contextBridge
  window.ipcRenderer.on('main-process-message', (_event, message) => {
    console.log(message)
  })
})



