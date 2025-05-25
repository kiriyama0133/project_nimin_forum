<script setup lang="ts">
import { onMounted, ref } from 'vue';
import loading from '../components/Common/loading.vue';
import menubarcomponent from '../components/Menubar/menubarcomponent.vue';
import 'primeicons/primeicons.css';
import menucomponet from '../components/Menubar/menucomponet.vue';
import { useRouter } from 'vue-router';
import Drawer from 'primevue/drawer';
import { useDrawerStore} from '../stores/drawer'
import Button from 'primevue/button';
import { Cookie, CookieResponse } from '../types/cookies';
import { fetchUserCookies } from '../utils/getCookies';
import {useCounterStore} from '../stores/login_register';
import { useCarddata } from '../stores/carddata';
import axiosInstance from '../utils/getCards';
import { isloading as loadingStore } from '../stores/isloading';

const drawerStore = useDrawerStore()
const router = useRouter()
let isloading = ref(true);
const userStore = useCounterStore();
const cardstore = useCarddata();
const isloadingstore = loadingStore();

interface CookieInfo {
  id: string;
  name: string;
  status: 'available' | 'in-use' | 'banned';
  reason?: string;
}
const userCookies = ref<CookieInfo[]>([]);
const bannedCookies = ref<CookieInfo[]>([]);
const isLoading = ref(false);
const fetchUserCookieData = async () => {
  isLoading.value = true;
  try {
    const response: CookieResponse = await fetchUserCookies();
    
    userCookies.value = [];
    bannedCookies.value = [];

    const fetchedCookies: Cookie[] = response.data;
   //console.log("Fetched cookies from backend:", fetchedCookies);

    fetchedCookies.forEach(backendCookie => {
      if (backendCookie.isbanned) {
        bannedCookies.value.push({
          id: backendCookie.name,
          name: backendCookie.name,
          status: 'banned',
        });
      } else {
        userCookies.value.push({
          id: backendCookie.name,
          name: backendCookie.name,
          status: backendCookie.inused ? 'in-use' : 'available',
        });
        userStore.userInfo.username = userCookies.value.find(c => c.status === 'in-use')?.name || '';
        console.log("检测到了现在正在使用",userStore.userInfo.username)
      }
    });
    //console.log("Cookie data processed from backend.");
  } catch (error: any) {
    console.error('Failed to fetch user cookie data:', error);
    userCookies.value = [];
    bannedCookies.value = [];
  } finally {
    isLoading.value = false;
  }
};
let screenWidth = ref(window.innerWidth)
onMounted(() => {
   window.addEventListener('resize', updateScreenWidth);
   // Redirect logic on mount
   if (router.currentRoute.value.path === '/' || router.currentRoute.value.path === '/homepage') {
      router.push('/Introduction');
   }
   check_loading();
   fetchUserCookieData();
   // 在进入页面时加载综合板内容
   cardstore.carddata.splice(0, cardstore.carddata.length);
   isloadingstore.dataloading = true;
   cardstore.category = 'total';
   isloadingstore.dataend = false;
   axiosInstance.post('/getcard', { skip: 0, category: 'total' }).then((response) => {
      const receivedCards = response.data.data;
      if (receivedCards && Array.isArray(receivedCards)) {
         cardstore.carddata.push(...receivedCards);
         if (receivedCards.length < 5) {
            isloadingstore.dataend = true;
         }
      }
   }).catch(error => {
      console.error('加载初始数据失败:', error);
   }).finally(() => {
      isloadingstore.dataloading = false;
   });
});
function updateScreenWidth() {screenWidth.value = window.innerWidth;console.log(screenWidth.value) }// 更新屏幕宽度

function check_loading(){
   let timer = setInterval(() => {
      if(document.readyState === 'complete')     // 判断页面是否加载完成 定时器
      {
         const loadingElement = document.getElementById('loading');
         if (loadingElement) {
            // 延迟触发动画
            setTimeout(() => {
               loadingElement.style.opacity = '0'; // 目标透明度
               loadingElement.style.backgroundColor = 'rgba(255, 255, 255, 0)';
            }, 0); // 延迟 0 毫秒，确保初始样式生效
         setTimeout(() => {
            clearInterval(timer);
            isloading.value = false;
         }, 300);
         }
      }
   }, 300);
}

</script>
<template>
<div class="main-page h-screen flex flex-col bg-gray-100 homepage">
   <meta name="viewport" content="width=device-width, initial-scale=1,user-scalable=no,maximum-scale=1"> <!-- 禁止缩放 以及允许滚动-->
   <div class="flex-shrink-0 bg-white/80 shadow-md z-10 backdrop-blur-sm">
      <menubarcomponent/>
      <div class="relative">
         <Button v-if="screenWidth < 430" class="fixed top-1/4 -left-2 transform 
         translate-y-[0%] rounded-full w-12 h-10 bg-white/80 shadow-lg p-0 flex items-center justify-center 
         text-gray-600 hover:bg-gray-50 z-50 backdrop-blur-sm" @click="drawerStore.Drawervisible = true" aria-label="Open Menu">
            <i class="pi pi-arrow-right text-xl"/>
         </Button>
      </div>
   </div>
   <div class="flex flex-1 overflow-hidden">
      <div class="w-60 flex-shrink-0 overflow-y-auto scroll-custom bg-white/80 shadow backdrop-blur-sm" v-if="screenWidth > 425">
         <menucomponet/>
      </div>
      <div class="flex-1 overflow-y-auto scroll-custom p-4 md:p-6 router-view-container">
         <router-view v-slot="{ Component }">
            <transition name="fade" mode="out-in">
               <component :is="Component" />
            </transition>
         </router-view>
      </div>
   </div>

   <loading v-if="isloading" id="loading"/>
   <Drawer class="scroll-custom" v-model:visible="drawerStore.Drawervisible" header="♥😄🤭">
      <menucomponet/>
   </Drawer>
</div>

</template>

<style scoped lang="sass">
@import "bootstrap/scss/bootstrap";
</style>
<style lang="css">
.scroll-custom::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
.scroll-custom::-webkit-scrollbar-thumb {
   background-color: #a0aec0;
   border-radius: 3px;
}
.scroll-custom::-webkit-scrollbar-track {
   background-color: #f7fafc;
   border-radius: 3px;
  }

/* 添加毛玻璃效果支持 */
.backdrop-blur-sm {
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

/* 深色模式适配 */
:root[class~="darkmode"] .bg-white\/80 {
  background-color: rgba(17, 24, 39, 0.8);
}

:root[class~="darkmode"] .text-gray-600 {
  color: #e5e7eb;
}

:root[class~="darkmode"] .hover\:bg-gray-50:hover {
  background-color: rgba(31, 41, 55, 0.8);
}

body{
   position: relative; 
   cursor: url('@/assets/ani/select_2.png'), pointer;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>