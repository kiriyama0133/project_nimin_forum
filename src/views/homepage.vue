<script setup lang="ts">
import { onMounted, ref } from 'vue';
import loading from '../components/loading.vue';
import Menubar from 'primevue/menubar';
import Menu from 'primevue/menu';
import 'primeicons/primeicons.css';
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

const items = ref([
    {
        label: 'Documents',
        items: [
            {
                label: 'New',
                icon: 'pi pi-plus'
            },
            {
                label: 'Search',
                icon: 'pi pi-search'
            }
        ]
    },
    {
        label: 'Profile',
        items: [
            {
                label: 'Settings',
                icon: 'pi pi-cog'
            },
            {
                label: 'Logout',
                icon: 'pi pi-sign-out'
            }
        ]
    },
    {
        label: 'Home',
        icon: 'pi pi-home'
    },
    {
        label: 'Features',
        icon: 'pi pi-star'
    },
    {
        label: 'Projects',
        icon: 'pi pi-search',
        items: [
            {
                label: 'Components',
                icon: 'pi pi-bolt'
            },
            {
                label: 'Blocks',
                icon: 'pi pi-server'
            },
            {
                label: 'UI Kit',
                icon: 'pi pi-pencil'
            },
            {
                label: 'Templates',
                icon: 'pi pi-palette',
                items: [
                    {
                        label: 'Apollo',
                        icon: 'pi pi-palette'
                    },
                    {
                        label: 'Ultima',
                        icon: 'pi pi-palette'
                    }
                ]
            }
        ]
    },
    {
        label: 'Contact',
        icon: 'pi pi-envelope'
    }

]);
const items_ = ref([
   
    {
        label: 'Home',
        icon: 'pi pi-home'
    },
    {
        label: 'Features',
        icon: 'pi pi-star'
    },
    {
        label: 'Projects',
        icon: 'pi pi-search',
        items: [
            {
                label: 'Components',
                icon: 'pi pi-bolt'
            },
            {
                label: 'Blocks',
                icon: 'pi pi-server'
            },
            {
                label: 'UI Kit',
                icon: 'pi pi-pencil'
            },
            {
                label: 'Templates',
                icon: 'pi pi-palette',
                items: [
                    {
                        label: 'Apollo',
                        icon: 'pi pi-palette'
                    },
                    {
                        label: 'Ultima',
                        icon: 'pi pi-palette'
                    }
                ]
            }
        ]
    },
    {
        label: 'Contact',
        icon: 'pi pi-envelope'
    }
]);
</script>
<template>
   <meta name="viewport" content="width=device-width, initial-scale=1,user-scalable=no,maximum-scale=1"> <!-- 禁止缩放 以及允许滚动-->
   <div class="container-bluid">
      <div class="row">
         <div class="col-12">
            <Menubar :model="items_" >
               
               <template #end>
                  <div class="flex items-center gap-5">
                     <span class=" bg-amber-100">1</span>
                     <span>2</span>
                  </div>
               </template>
            </Menubar>
         </div>
      </div>
   </div>
   <div class="container-bluid">
      <div class="row">
         <div class="col-1" v-if="screenWidth > 425">
            <Menu :model="items" class=" w-50" />
         </div>
      </div>
    </div>
    <loading v-if="isloading" id="loading"/>
</template>

<style scoped lang="sass">
@import "bootstrap/scss/bootstrap";
</style>