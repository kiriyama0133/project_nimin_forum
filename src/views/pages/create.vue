<script setup lang="ts">
import subcltureheader from '@/components/Headers/subcltureheader.vue';
import defaultcard from '@/components/Cards/defaultcard.vue';
import axiosInstance from '@/utils/getCards'
import {useCarddata} from '@/stores/carddata'
import { ref } from 'vue';
import { isloading } from '@/stores/isloading';
import SendTopicDialog from '@/components/Dialogs/SendTopicDialog.vue';

const isloadingstore = isloading();
const cardstore = useCarddata();
let dataloading = ref(false);

//刷新卡片
function refresh(path: string, api: string, category: string) {
    console.log(`刷新分类: ${category}, 路径: ${path}, API: ${api}`);
    cardstore.carddata.splice(0, cardstore.carddata.length); // 清空列表
    isloadingstore.dataloading = true; // This can remain if used for other global state
    dataloading.value = true; // Controls the spinner
    cardstore.category = category;//设置分类
    isloadingstore.dataend = false;
    //第一次加载内容
    axiosInstance.post(api, { skip: 0, category: category }).then((response) => {
        const receivedCards = response.data.data;
        if (receivedCards && Array.isArray(receivedCards)) {
            cardstore.carddata.push(...receivedCards);
            console.log(`分类 "${category}" 的初始卡片数据已加载:`, cardstore.carddata);
            if (receivedCards.length < 5) {
                console.log("分类",category,"的卡片数据不足5条，已设置为已结束。")
                isloadingstore.dataend = true;
            }
        } else {
            console.warn(`分类 "${category}" 返回的初始卡片数据无效或为空:`, receivedCards);
        }
    }).catch(error => {
        console.error(`从 ${api} (分类: ${category}) 刷新初始数据失败:`, error);
    }).finally(() => {
        dataloading.value = false;
    });
}

//发送请求获得前5个卡片数据
const submitregister = async () => {
  dataloading.value = true;
  try {
    const currentItemCount = cardstore.carddata.length;
    console.log(`请求下一页，跳过: ${currentItemCount}`);

    const response = await axiosInstance.post('/getcard', { skip: currentItemCount,category:cardstore.category });
    const receivedCards = response.data.data;

    if (receivedCards && Array.isArray(receivedCards)) {
      cardstore.carddata.push(...receivedCards);
      console.log('已添加数据：', receivedCards);
      console.log('目前总卡片数据：', cardstore.carddata);
      if (receivedCards.length === 0) {
        isloadingstore.dataend = true;
      }
    } else {
      console.log('未收到卡片数据或格式不正确。', receivedCards);
    }
    
  } catch (error) {
    console.error('请求失败:', error);
  } finally {
    dataloading.value = false;
  }
};

// 滚动事件处理函数
const scrollContainer = ref<HTMLElement | null>(null);
const handleScroll = () => {
  if (!scrollContainer.value) return;
  const scrollTop = scrollContainer.value.scrollTop;
  const clientHeight = scrollContainer.value.clientHeight;
  const scrollHeight = scrollContainer.value.scrollHeight;
  if (scrollTop + clientHeight >= scrollHeight - 10) {
    onScrollToBottom();
  }
};

const onScrollToBottom = () => {
  if (isloadingstore.dataend || dataloading.value) {
    return;
  }
  console.log("滚动到底部了！准备延时加载...");
  dataloading.value = true;
  setTimeout(() => {
    if (dataloading.value && !isloadingstore.dataend) {
        console.log("延时结束，开始获取下一页数据...");
        submitregister();
    } else {
        console.log("延时期间加载状态改变，取消本次数据获取。");
        if (dataloading.value) dataloading.value = false;
    }
  }, 1000); 
};

const showDialog = ref(false);
const handleTopicSent = () => {
    refresh('/subculture', '/getcard', cardstore.category);
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