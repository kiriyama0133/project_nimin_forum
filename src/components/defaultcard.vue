<template>
<div>
    <div @click="refresh('/contentpage','/getsendCard')" class="defaultcard bg-pink-50 rounded-lg shadow-lg transition-all 
        duration-500 transform hover:shadow-2xl hover:-translate-y-2 h-[10rem] line-clamp-5">
        <div class="p-4">
            <h2 class="text-lg  text-gray-800 mb-4">
                <slot name="title">
                    <div class="flex gap-4">
                        <p>No.{{ number }}</p>
                        <p>{{ id }}</p>
                    </div>
                </slot>
            </h2>
            <p class="text-gray-600">
               <slot name="content">
                <p>{{ content }}</p>
               </slot>
            </p>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
defineProps(['number','id','content'])
import { useRouter } from 'vue-router';
import axiosInstance from '../utils/getReply'
import {useCarddata} from '../stores/contentsotre'
const sendcardstore = useCarddata()
const router = useRouter()
function refresh(path:string,api:string) {
    sendcardstore.contentdata.splice(0,sendcardstore.contentdata.length); //清空列表
    router.push(path);
    axiosInstance.get(api).then((response)=>{
        sendcardstore.contentdata.push(response.data)
    })
}
</script>
<style scoped>
.defaultcard{
cursor: url('../assets/ani/link_2.png'), pointer;
}
</style>