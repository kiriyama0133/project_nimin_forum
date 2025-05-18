<script setup lang="ts">
import routecard from '../components/routecard.vue';
import { onMounted, ref, watch } from 'vue';
import {useCounterStore} from '../stores/login_register'
import routate from '../components/routate.vue';
import login from './login.vue';
import register from './register.vue';
import reset from '../components/reset.vue';
import { useRouter } from 'vue-router';
import { LoginService, OpenAPI } from '../client';
import { getUserIdFromToken } from '../utils/fromTokenGetID';
import loading from '../components/loading.vue';
// 获取用户id
const userId = getUserIdFromToken();
const store = useCounterStore();
const router = useRouter();
store.userInfo.username = userId;

let screenWidth = ref(window.innerWidth)
onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
  checkExistingToken();
});

function animateElement(translateX:any, opacity:any, duration:any) {
  const element = document.getElementById("shrinkable-component");
    if(element != null){// 动态设置动画持续时间
    element.style.transition = `transform ${duration}ms ease, opacity ${duration}ms ease`;
    // 设置平移和透明度
    element.style.transform = `translateX(${translateX}px)`;
    element.style.opacity = opacity;
 }
}

function animateElement_R(translateX:any, opacity:any, duration:any) {
  const element = document.getElementById("shrinkable-component");
    if(element != null){// 动态设置动画持续时间
    element.style.transition = `transform ${duration}ms ease, opacity ${duration}ms ease`;
    // 设置平移和透明度
    element.style.transform = `translateX(${translateX}px)`;
    element.style.opacity = opacity;
 }
}
function updateScreenWidth() {screenWidth.value = window.innerWidth;console.log(screenWidth.value) }// 更新屏幕宽度

//检查现有的token，如果有就发送至服务端去验证
const checkExistingToken = async () => {
  const token = localStorage.getItem('access_token');
  if (token) {
    console.log('Found token, verifying...');
    store.loading = true;
    OpenAPI.TOKEN = token;
    try {
      await LoginService.testToken();
      console.log('Token verified successfully.');
      router.push('/homepage');
    } catch (error) {
      console.error('Token verification failed:', error);
      localStorage.removeItem('access_token');
      OpenAPI.TOKEN = undefined;
    } finally {
      store.loading = false;
    }
  } else {
    console.log('No existing token found.');
  }
};

let form = ref('login')

watch(()=>store.homepage, (newValue, _) => {
    if (newValue=='register') {
      console.log("register_form!")
      animateElement(200, 0, 300)
      setTimeout(() => {
        form.value = 'register'
        animateElement_R(0, 1, 300)
      }, 320);
    }
    if (newValue=='login') {
      console.log("login_form!")
      animateElement(200, 0, 300)
      setTimeout(() => {
        form.value = 'login'
        animateElement_R(0, 1, 300)
      }, 320);
    }
    if (newValue=='reset') {
      console.log("reset_form!")
      animateElement(200, 0, 300)
      setTimeout(() => {
        form.value = 'reset'
        animateElement_R(0, 1, 300)
      }, 320);
    }
});

</script>

<template>
    <loading v-if="store.loading"/>
    <div class="cursor-window">
        <div class="bg-white opacity-40 w-full overflow-hidden">
            <div class="bg-[url('@/assets/bg/marshmary.jpg')] bg-cover w-screen h-screen overflow-hidden">
                <div class="grid grid-cols-16">
                    <div v-if="screenWidth>425" class="route-div z-10 col-span-10 overflow-hidden flex justify-center items-center ">
                        <routecard id="orbit" class="orbit rotate-x-50 rotate-z-45 transition-normal duration-300 hover:rotate-x-0 hover:rotate-z-0"></routecard>
                        <routate class="rotate overflow-hidden h-screen"/>
                        
                    </div>
                <div class="login z-11 col-span-6 w-full bg-white opacity-70 
                    backdrop-blur-2xl ease-in-out h-screen transition duration-500 
                    hover:opacity-90 drop-shadow-2xl">
                    <div id="shrinkable-component" class="shrinkable-component">
                        <login class="card" v-if="form=='login'"></login>
                        <register class="card" v-if="form=='register'"></register>
                        <reset class="card" v-if="form=='reset'"></reset>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.orbit{
    position: absolute;
    top:20%
}
.rotate {
  position: absolute;
  z-index: 10;
}
.cursor-window {
    cursor: url('../assets/ani/select_2.png'), pointer;
}

</style>