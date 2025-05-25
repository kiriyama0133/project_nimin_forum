<script setup lang="ts">
import { ref, watch } from 'vue';
import 'primeicons/primeicons.css';
import Button from 'primevue/button';
import Menubar from 'primevue/menubar';
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import InputGroupAddon from 'primevue/inputgroupaddon';
import Popover from 'primevue/overlaypanel'; // Popover 实际是 OverlayPanel
import { useRouter, useRoute } from 'vue-router';
import { OpenAPI } from '../../client/core/OpenAPI';
import { ElMessage } from 'element-plus';
import FontSettings from '../Preferences/FontSettings.vue';
import type { UserCardRequest, UserCardResponse } from '@/types/sendcard.d';
import { useCounterStore } from '@/stores/login_register';
import { getUserCard } from '@/utils/getCards';
import { useCarddata } from '@/stores/carddata';
import { isloading } from '@/stores/isloading';
import axiosInstance from '@/utils/getCards'
const isloadingstore = isloading();
const store = useCounterStore();
const router = useRouter()
const route = useRoute()
const cardstore = useCarddata();
import { useToast } from "primevue/usetoast";
const toast = useToast();
let dataloading = ref(false);
// 获取当前URL
let currentUrl = ref(window.location.href);
function refresh(path: string, api: string) {
    console.log(`路径: ${path}, API: ${api}`);
    cardstore.carddata.splice(0, cardstore.carddata.length); // 清空列表
    isloadingstore.dataloading = true; // This can remain if used for other global state
    dataloading.value = true; // Controls the spinner
    //console.log("当前的分类是：",cardstore.category)
    isloadingstore.dataend = false;
    //第一次加载内容
    axiosInstance.post(api, { skip: 0}).then((response) => {
        const receivedCards = response.data.data;
        if (receivedCards && Array.isArray(receivedCards)) {
            cardstore.carddata.push(...receivedCards);
            console.log(`的初始卡片数据已加载:`, cardstore.carddata);
            if (receivedCards.length < 5) {
                console.log("卡片数据不足5条，已设置为已结束。")
                isloadingstore.dataend = true;
            }
        } else {
            console.warn(`返回的初始卡片数据无效或为空:`, receivedCards);
            // Handle case where category might have no cards initially
        }
    }).catch(error => {
        console.error(`从 ${api} 刷新初始数据失败:`, error);
        toast.add({ severity: "error", summary: "错误", detail: "加载初始数据失败", life: 3000 });
    }).finally(() => {
        dataloading.value = false; // Hide spinner
        // cardstore.initialLoading = false; // Reset loading state if used
    });
}
// 监听路由变化
watch(
  () => route.fullPath,
  () => {
    currentUrl.value = window.location.href;
  }
);
// 复制URL功能
const copyCurrentUrl = () => {
  navigator.clipboard.writeText(currentUrl.value).then(() => {
    ElMessage({
      message: '链接已复制到剪贴板',
      type: 'success',
      duration: 2000
    });
  }).catch(() => {
    ElMessage({
      message: '复制失败，请手动复制',
      type: 'error',
      duration: 2000
    });
  });
};

const items_ = ref([
   {
       label: '主页',
       icon: 'pi pi-home',
       command:()=>{
        router.push('/Introduction')
    }
   },
   {
       label: '搜索',
       icon: 'pi pi-search',
       command:()=>{
        router.push('/search')
    }
    },
]);

const op = ref();
const toggle = (event:any) => {
    op.value.toggle(event);
}
function DeleteToken() {
    localStorage.removeItem('access_token');
    OpenAPI.TOKEN = undefined;
    router.push('/loginview')
}
async function UserCard() {
    const request: UserCardRequest = {
        Cookie: store.userInfo.username,
        skip: 0
    }
    const response:UserCardResponse = await getUserCard(request);
    // 清空数组
    cardstore.UserCard.defaultcard = [];
    cardstore.UserCard.addreplycard = [];
    cardstore.UserCard.defaultcard.push(...response.DefaultCard);
    cardstore.UserCard.addreplycard.push(...response.AddReplyCard);
    router.push('/mycard')
}
const showFontSettings = ref(false);
</script>
<template>
<Menubar :model="items_" breakpoint="520px" :base-z-index="90">
  
    <template #end>
        <div class="flex items-center gap-2">
            <div class="flex gap-2 items-center">
                <Button @click="router.push('/cookies')" :pt="{
                    root:{class: 'btn-cursor'}
                }" variant="outlined" raised style="font-size: 10px;" 
                class="text w-23 h-8" label="饼干管理" icon="pi pi-user" />
            </div>

        <div id="user-info" class="">
            <div class="card flex justify-center">
                <Button :pt="{
                    root:{class: 'btn-cursor'}
                }" variant="outlined" raised class="w-18 h-8" 
                style="font-size: 10px;" type="button" icon="pi pi-user" label="操作" @click="toggle" />
                    <Popover :base-z-index="90" ref="op">
                        <div class="flex flex-col gap-1 w-[16rem]">

                            <div>
                                <span class="font-medium block mb-2">分享这个贴</span>
                                <InputGroup>
                                    <InputText :value="currentUrl" readonly class="w-[16rem]"></InputText>
                                    <InputGroupAddon @click="copyCurrentUrl" class="cursor-pointer">
                                        <i class="pi pi-copy"></i>
                                    </InputGroupAddon>
                                </InputGroup>
                            </div>

                            <div>
                                <span class="font-medium block mb-2">历史操作和偏好</span>
                                <div class="grid grid-cols-2 gap-2">
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的回复"  icon="pi pi-reply" @click="UserCard"/>
                                    <Button variant="outlined"  raised style="font-size: 16px;" 
                                    class="text w-30 h-8" label="我的收藏" 
                                    icon="pi pi-star" @click="refresh('/favorite','/getfavoritecard'),router.push('/favorite')" />
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="偏好设置" icon="pi pi-cog" @click="router.push('/preferences')" />
                                    <Button @click="DeleteToken" variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="退出账号" icon="pi pi-sign-out" />
                                </div>
                            </div>

                        </div>
                    </Popover>
                </div>
            </div>
        </div>
    </template>
</Menubar>

<FontSettings v-if="showFontSettings" @close="showFontSettings = false" />
</template>
<style>
.text{
    font-size: 20px;
}
.btn-cursor {
cursor: url('../assets/ani/link_2.png'), pointer;
}
.p-button, .p-button * {
  cursor: url('@/assets/ani/link_2.png'), pointer !important;
}
</style>