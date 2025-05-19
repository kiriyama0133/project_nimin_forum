<template>
<div class=" rounded-lg">
    <div class="defaultcard bg-gray-300 rounded-lg shadow-lg transition-all 
        duration-500 transform hover:shadow-2xl hover:-translate-y-2 ">
        <div  @click="gotoreply" class="p-4">
            <h2 class="text-lg  text-gray-800 mb-4">
                <slot name="title">
                    <div class="flex gap-4 justify-between">
                        <div>
                            <p class="Mate">No.{{ props.number }}</p>
                            <p class="User_Id">{{ props.id }}</p>
                        </div>
                            <p class="Mate" style="font-size: xx-small;">{{ props.time }}</p>
                         </div>
                </slot>
            </h2>
            <p class="text-gray-600 line-clamp-3 min-h-[4.5rem]">
               <slot name="content">
                <p class="content-text">{{ props.content }}</p>
               </slot>
            </p>
            <div v-if="props.imageUrls && props.imageUrls.length > 0" class="mt-2 flex flex-wrap gap-2 max-h-24 overflow-y-auto">
                <img 
                    v-for="(relativePath, index) in props.imageUrls" 
                    :key="index" 
                    :src="`${IMAGE_BASE_URL}${relativePath}`" 
                    :alt="`Image ${index + 1}`" 
                    class="h-20 w-20 object-cover rounded border border-gray-300 cursor-pointer"
                    @click.stop="openImageModal(`${IMAGE_BASE_URL}${relativePath}`)" 
                />
            </div>
            </div>
            
            <div class ="flex justify-end h-5 items-center pr-2 pb-1">
                <ToggleButton size="small" v-model="isfavorate" 
                @change="favorite()" onIcon="pi pi-star-fill" 
                offIcon="pi pi-star" onLabel="已收藏" offLabel="收藏"/>
            </div>
        </div>
    </div>

    <Dialog v-model:visible="isImageModalVisible" modal header="图片预览" :style="{ width: '90vw', maxWidth: '800px' }">
        <img :src="currentModalImageUrl" alt="Full image preview" class="w-full h-auto max-h-[80vh] object-contain" />
    </Dialog>
</template>
<script lang="ts" setup>
const props = defineProps<{ 
    number: string | number;
    id: string;
    content: string;
    time: string;
    thumbs?: string | number;
    imageUrls?: string[]; 
}>();

import { useRouter } from 'vue-router';
import  'primeicons/primeicons.css'
import ToggleButton from 'primevue/togglebutton';
import Dialog from 'primevue/dialog';
import { ref,onMounted } from 'vue'
import { toggleFavorite } from '../utils/favorite';
import axiosInstance from '../utils/favoritestatus';
import { ca } from 'element-plus/es/locale/index.mjs';
const IMAGE_BASE_URL = import.meta.env.VITE_API_URL + '/i/';
const router = useRouter()
const isfavorate = ref(false)
const isImageModalVisible = ref(false);
const currentModalImageUrl = ref('');
const gotoreply = ()=>{
    router.push({
    name: '内容页',
    query: {
      number: props.number,
      time: props.time,
    }
  });
};

const openImageModal = (imageUrl: string) => {
    currentModalImageUrl.value = imageUrl;
    isImageModalVisible.value = true;
};

const favorite =async ()=>{
    const isNowfavorate = isfavorate.value
    console.log(isNowfavorate)
    try{
        await toggleFavorite({ 
            card_number: Number(props.number),
            action: isNowfavorate ? 'favorate' : 'unfavorate'
        })
        console.log(isNowfavorate?'收藏成功':'取消收藏成功')
    }
    catch(error){
        console.error("收藏失败",error)
    }
}
const checkfavorite =async()=>{
    try{
        const response= await axiosInstance.get('/favoratestatus',{
            params:{
                card_number: props.number
            }
        })
        isfavorate.value = response.data.isfavorate
    }
    catch(error){
        console.error('获取收藏状态失败:',error)
    }
}
onMounted(()=>{
    checkfavorite()
})
</script>
<style scoped>
.defaultcard{
cursor: url('../assets/ani/link_2.png'), pointer;
}
.Mate {
  font-weight: inherit;
  transition: color 0.2s ease;
}
.content-text {
  font-weight: inherit;
  transition: color 0.2s ease;
}
.User_Id {
  font-weight: inherit;
  transition: color 0.2s ease;
}
</style>