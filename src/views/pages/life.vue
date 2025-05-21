<script setup lang="ts">
import subcltureheader from '@/components/Headers/subcltureheader.vue';
import defaultcard from '@/components/Cards/defaultcard.vue';
import {useCarddata} from '@/stores/carddata'
import { ref } from 'vue';
import { isloading } from '@/stores/isloading';
import SendTopicDialog from '@/components/Dialogs/SendTopicDialog.vue';
import { useInfiniteScroll } from '@/utils/infiniteScroll';

const isloadingstore = isloading();
const cardstore = useCarddata();
let dataloading = ref(false);
const scrollContainer = ref<HTMLElement | null>(null);

const { refresh, handleScroll } = useInfiniteScroll({
  scrollContainer,
  dataloading,
  cardstore,
  isloadingstore
});

const showDialog = ref(false);
const handleTopicSent = () => {
    refresh('/life', '/getcard', cardstore.category);
};
</script>

<template>
    <div @scroll="handleScroll"
    ref="scrollContainer" class="subculture scroll-custom h-full overflow-y-auto relative">
        <div name="header">
            <subcltureheader>
                <template #header>
                    <!-- 如果不适用插槽则显示默认内容,这里打算用v-html去渲染内容，由接口服务 -->
                </template>
            </subcltureheader>
        </div>

        <div name="content" class="flex flex-col gap-2 p-2">
            <defaultcard v-for="item in cardstore.carddata"
                :key="item.id"
                :number="item.number"
                :time="item.time"
                :id="item.id"
                :content="item.content"
                :thumbs="item.thumbs"
                :imageUrls="item.imageUrls || []"
            >
            </defaultcard>
        </div>

        <div v-if="cardstore.carddata.length === 0 && !dataloading && isloadingstore.dataend" class="text-center p-5 text-gray-500">
            这个板块还没有内容哦~
        </div>

        <div v-if="isloadingstore.dataend && cardstore.carddata.length > 0" class="h-20 flex justify-center items-center text-gray-500">
            <p>内容已经加载完了~~ </p>
        </div>
        <div v-if="dataloading" class="flex justify-center h-20 py-4 items-center">
            <div class="flex flex-col items-center">
                <div class="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin" style="border-radius: 50%;"></div>
                <p class="mt-4 text-gray-600">加载中...</p>
            </div>
        </div>
        <div class="h-20"></div>

        <button
            @click="showDialog = true"
            title="发送话题"
            class="fixed bottom-5 right-5 w-10 h-10 bg-black text-white rounded-full shadow-lg
                   flex items-center justify-center
                   hover:bg-gray-700 transition-colors duration-200 z-20">
            <i class="pi pi-send text-xl"></i>
        </button>

        <SendTopicDialog
            v-model="showDialog"
            :category="cardstore.category"
            @topicSent="handleTopicSent"
        />
    </div>
</template>

<style scoped>
.subculture{
cursor: url('@/assets/ani/select_2.png'), pointer;
}
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