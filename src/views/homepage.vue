<script setup lang="ts">
import { onMounted, ref } from 'vue';
import loading from '../components/loading.vue';
import menubarcomponent from '../components/menubarcomponent.vue';
import 'primeicons/primeicons.css';
import menucomponet from '../components/menucomponet.vue';
let isloading = ref(true);

let screenWidth = ref(window.innerWidth)
onMounted(() => {window.addEventListener('resize', updateScreenWidth);});
function updateScreenWidth() {screenWidth.value = window.innerWidth;console.log(screenWidth.value) }// 更新屏幕宽度
 
function check_loading(){
   let timer = setInterval(() => {
      if(document.readyState === 'complete')     // 判断页面是否加载完成 定时器
      {
         const loading = document.getElementById('loading');
         if (loading) {
            // 延迟触发动画
            setTimeout(() => {
               loading.style.opacity = '0'; // 目标透明度
               loading.style.backgroundColor = 'rgba(255, 255, 255, 0)';
            }, 0); // 延迟 0 毫秒，确保初始样式生效
         setTimeout(() => {
            clearInterval(timer);
            isloading.value = false;
         }, 300);
         }
      }
   }, 300);
}
onMounted(() => {
   check_loading();
});

</script>
<template>
<body class="overflow-hidden h-screen" style="z-index: 90;">
   <meta name="viewport" content="width=device-width, initial-scale=1,user-scalable=no,maximum-scale=1"> <!-- 禁止缩放 以及允许滚动-->
   <div class="container-bluid">
         <div class="col-12">
            <menubarcomponent/>
         </div>
   </div>

   <div class="flex h-full" style="z-index: 80;">
      <div class="scroll-custom overflow-x-hidden overflow-y-scroll " v-if="screenWidth > 425">
         <menucomponet/>
      </div>
      <div class="p-4 w-full overflow-x-hidden overflow-y-scroll">
         <div alt="内容展示页面" class="">
            <span>123</span>
         </div>
      </div>
   </div>
   <loading v-if="isloading" id="loading"/>
</body>
</template>

<style scoped lang="sass">
@import "bootstrap/scss/bootstrap";
</style>
<style lang="css">
.scroll-custom::-webkit-scrollbar {
    width: 4px;
    height: 8px;
  }
  .scroll-custom::-webkit-scrollbar-thumb {
    background-color: #4b5563;
    border-radius: 4px;
  }
  .scroll-custom::-webkit-scrollbar-track {
    background-color: #e5e7eb;
    border-radius: 4px;
  }
</style>