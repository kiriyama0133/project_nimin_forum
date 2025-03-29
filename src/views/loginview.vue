<script setup lang="ts">
import routecard from '../components/routecard.vue';
import { watch } from 'vue';
import gsap from "gsap";
import {useCounterStore} from '../stores/login_register'
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
import { useRouter } from 'vue-router';
import routate from '../components/routate.vue';
import login from './login.vue';
import register from './register.vue';
const store = useCounterStore();
const router = useRouter();
// 注册 GSAP 插件
gsap.registerPlugin(MotionPathPlugin);
// function scaleComponent(scale:any, duration:any) {
//   const component = document.getElementById('shrinkable-component');
//   if (component) {
//     component.style.transition = `transform ${duration}ms ease`; // 动态设置过渡时间
//     component.style.transform = `scale(${scale})`; // 动态设置缩放比例
//   }
// }
watch(()=>store.homepage, (newValue, _) => {
    if (newValue=='register') {
      console.log("ok!")

    }

    if(newValue=='login'){

    }
});

</script>

<template>
    <div class="cursor-window overflow-hidden ">
        <div class="bg-white opacity-40 w-full overflow-hidden">
            <div class="bg-[url('src/assets/bg/marshmary.jpg')] bg-cover w-screen h-screen overflow-hidden">
                <div class="grid grid-cols-15">
                    <div class="route-div col-span-7 overflow-hidden flex justify-center items-center ">
                        <routecard id="orbit" class="orbit rotate-x-50 rotate-z-45 transition-normal duration-300 hover:rotate-x-0 hover:rotate-z-0"></routecard>
                        <routate class="rotate overflow-hidden h-screen"/>
                    </div>
                <div class="col-span-2 bg-[linear-gradient(to_left,rgba(255,255,255,0.9),rgba(255,255,255,0))]"></div>
                <div class="login col-span-6 w-full bg-white opacity-70 
                    backdrop-blur-2xl ease-in-out h-screen transition duration-500 
                    hover:opacity-85 drop-shadow-2xl">
                    <div id="shrinkable-component" class="shrinkable-component">

                            <login class="card" v-if="store.homepage=='login'"></login>
                            <register class="card" v-if="store.homepage=='register'"></register>
  
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.shrinkable-component {
  transition: transform 2s ease; /* 设置过渡效果 */
}
.orbit{
    position: absolute;
    top:20%
}
.rotate {
  position: absolute;
  z-index: 10;
}
.cursor-window {
    cursor: url('../assets/ani/select.png'), pointer;
}

</style>