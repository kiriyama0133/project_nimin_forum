<template>
<div class=" rounded-lg" style="box-shadow: 0 0 10px 5px rgba(255, 255, 255, 0.5);">
    <div class="defaultcard bg-pink-50 rounded-lg shadow-lg transition-all 
        duration-500 transform hover:shadow-2xl hover:-translate-y-2 h-[10rem] line-clamp-5">
        <div  @click="refresh('/contentpage','/getsendCard')" class="p-4">
            <h2 class="text-lg  text-gray-800 mb-4">
                <slot name="title">
                    <div class="flex gap-4 justify-between">
                        <div>
                            <p>No.{{ number }}</p>
                            <p>id:{{ id }}</p>
                        </div>
                            <p style="font-size: xx-small;">{{ time }}</p>
                         </div>
                </slot>
            </h2>
            <p class="text-gray-600">
               <slot name="content">
                <p>{{ content }}</p>
               </slot>
            </p>
            </div>
            <div class ="flex justify-end h-5 items-center">
                <ToggleButton size="small" v-model="isfavorate" onIcon="pi pi-star-fill" offIcon="pi pi-star" onLabel="已收藏" offLabel="收藏"/>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
defineProps(['number','id','content','time'])
import { useRouter } from 'vue-router';
import axiosInstance from '../utils/getReply'
import {useCarddata} from '../stores/contentsotre'
import  'primeicons/primeicons.css'
import ToggleButton from 'primevue/togglebutton';
import { ref } from 'vue'
const sendcardstore = useCarddata()
const router = useRouter()
const isfavorate = ref(false)
function refresh(path:string,api:string) {
    sendcardstore.contentdata.splice(0,sendcardstore.contentdata.length); //清空列表
    router.push(path);
    axiosInstance.get(api).then((response)=>{
        sendcardstore.contentdata.push(response.data)
    })
    //这里之后写向后台请求点赞数据的业务代码。
}
function favorate(){

}
</script>
<style scoped>
.defaultcard{
cursor: url('../assets/ani/link_2.png'), pointer;
}
</style>