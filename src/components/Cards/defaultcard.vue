<template>
<div class=" rounded-lg">
    <div class="defaultcard bg-gray-200 rounded-lg shadow-lg transition-all 
        duration-500 transform hover:shadow-2xl hover:-translate-y-2 ">
        <div  @click="gotoreply" class="p-4 ">
            <h2 class="text-lg text-gray-800 mb-4">
                <slot name="title">
                    <div class="flex gap-4 justify-between">
                        <div>
                            <p class="Mate">No.{{ props.number }} {{ categoryDisplay ? `${categoryDisplay}` : '' }}</p>
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
                <ToggleButton size="small" v-model="isfavorite" 
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
import { useRouter } from 'vue-router';
import  'primeicons/primeicons.css'
import ToggleButton from 'primevue/togglebutton';
import Dialog from 'primevue/dialog';
import { ref, computed,onMounted } from 'vue'

const props = defineProps<{
    number: number;
    id: string;
    content: string;
    time: string;
    imageUrls: string[];
    category?: string;
    thumbs?: number;
}>();

// 分类映射表
const categoryMap = {
    // 综合版和时间板
    'total': '综合版',
    'time': '时间板',
    
    // 亚文化
    'brahmin': '婆罗门',
    'anime': '动漫',
    'movie_tv': '电影/电视剧',
    'vtuber': 'vtuber',
    'boardgame': '卡牌桌游',
    'tokusatsu': '特摄',
    'warhammer': '战锤',
    'modelkit': '胶佬',
    'railfan': '铁道厨',
    'vocaloid': 'VOCALOID',
    'touhou': '东方project',
    'kancolle': '舰娘',
    
    // 创作
    'trpg': '跑团',
    'creation': '创作',
    'creepypasta': '规则怪谈',
    'situation_puzzle': '海龟汤',
    'science': '科学',
    'literature': '文学',
    'music': '音乐',
    'ai': 'AI',
    'photography': '摄影',
    
    // 游戏
    'game_general': '游戏综合',
    'mobile_game': '手游',
    'nintendo': '任天堂',
    'galgame': 'Galgame',
    'blizzard': '暴雪游戏',
    'square_enix': 'SE',
    'valve': 'V社',
    'monster_hunter': '怪物猎人',
    'hypergryph': '鹰角',
    'mihoyo': '米哈游',
    'rhythm_game': '音游',
    'tencent_game': '腾讯游戏',
    
    // 生活
    'camping': '露营',
    'self_help': '自救互助',
    'cooking': '料理',
    'sports': '体育',
    'study': '学业',
    'diary': '日记',
    
    // 其他
    'other': '其他'
} as const;

// 计算属性：获取分类显示名称
const categoryDisplay = computed(() => {
    if (!props.category) return '';
    return categoryMap[props.category as keyof typeof categoryMap] || props.category;
});

import { toggleFavorite } from '../../utils/favorite';
import axiosInstance from '../../utils/favoritestatus';
import { ca } from 'element-plus/es/locale/index.mjs';
const IMAGE_BASE_URL = import.meta.env.VITE_API_URL + '/i/';
const router = useRouter()
const isfavorite = ref(false)
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
    const isNowfavorate = isfavorite.value
    console.log(isNowfavorate)
    try{
        await toggleFavorite({ 
            card_number: Number(props.number),
            action: isNowfavorate ? 'favorite' : 'unfavorite'
        })
        console.log(isNowfavorate?'收藏成功':'取消收藏成功')
    }
    catch(error){
        console.error("收藏失败",error)
        isfavorite.value=!isfavorite.value
    }
}
const checkfavorite =async()=>{
    try{
        const response= await axiosInstance.get('/favorite-status',{
            params:{
                card_number: props.number
            }
        })
        isfavorite.value = response.data.favorite
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
cursor: url('@/assets/ani/link_2.png'), pointer;
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
:root.darkmode .defaultcard{
    background-color: #01012b;
}
</style>