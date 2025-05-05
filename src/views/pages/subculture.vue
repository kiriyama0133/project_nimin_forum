<script setup lang="ts">
import subcltureheader from '../../components/subcltureheader.vue';
import defaultcard from '../../components/defaultcard.vue';
import axiosInstance from '../../utils/getCards'
import {useCarddata} from '../../stores/carddata'
import { onMounted, ref } from 'vue';
const cardstore = useCarddata();
let dataend = ref(false);
let dataloading = ref(false);
//发送请求获得前5个卡片数据
const submitregister = async () => {
  dataloading.value = true; // 开始加载
  try {
    const currentItemCount = cardstore.carddata.length;
    console.log(`Requesting next page with skip: ${currentItemCount}`);

    const response = await axiosInstance.post('/getcard', { skip: currentItemCount }); 
    
    const receivedCards = response.data.data;

    if (receivedCards && Array.isArray(receivedCards)) {
      cardstore.carddata.push(...receivedCards);
      console.log('已添加数据：', receivedCards);
      console.log('目前总卡片数据：', cardstore.carddata);
      if (receivedCards.length === 0) {
        dataend.value = true; // 设置数据结束标志
      }
    } else {
      console.log('未收到卡片数据或格式不正确。', receivedCards);
      dataend.value = true; // Assume end if format is wrong
    }
    
  } catch (error) {
    console.error('请求失败:', error);
    dataend.value = true; // Assume end on error to prevent infinite loops
  } finally {
    dataloading.value = false; // 加载完成
  }
};
onMounted(()=>{
})
// 滚动事件处理函数
const scrollContainer = ref<HTMLElement | null>(null); // 定义模板引用
const handleScroll = () => {
  if (!scrollContainer.value) return; // 确保引用存在
  const scrollTop = scrollContainer.value.scrollTop;
  const clientHeight = scrollContainer.value.clientHeight;
  const scrollHeight = scrollContainer.value.scrollHeight;
//   console.log('滚动位置：', scrollTop);
//   console.log('容器高度：', clientHeight);
//   console.log('容器总高度：', scrollHeight);
  // 判断是否滚动到底部
  if (scrollTop + clientHeight >= scrollHeight) {
    onScrollToBottom();
  }
};

const onScrollToBottom = () => {
  console.log("滚动到底部了！");
  dataloading.value = true;
  setTimeout(() => {
    submitregister().then(()=>{
        console.log("数据加载完毕")
        dataloading.value = false;
}); //添加新一轮的数据
  // 在这里触发你的逻辑，比如加载更多数据
  }, 1000);
};
</script>
<template>
    <div @scroll="handleScroll"
    ref="scrollContainer" class="subculture scroll-custom h-full overflow-y-auto">
        <div name="header">
            <subcltureheader>
                <template #header>
                    <!-- 如果不适用插槽则显示默认内容,这里打算用v-html去渲染内容，由接口服务 -->
                </template>
            </subcltureheader>
        </div>

        <div name="content" class="flex flex-col gap-2 p-2">
            <defaultcard v-for="item in cardstore.carddata"
                :number="item.number"
                :time = "item.time"
                :id="item.id"
                :content="item.content"
            >
            </defaultcard>
        </div>

        <div v-if="dataend==true" class="h-50 flex justify-center">
            <p>内容已经加载完了~~ </p>
        </div>
            <div v-if="dataloading==true" class="flex justify-center h-100">
                <!-- 加载容器 -->
                <div class="flex flex-col items-center">
                <!-- 转圈动画 -->
                <div class="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
                <!-- 加载文字 -->
                <p class="mt-4 text-gray-600">加载中...</p>
            </div>
        </div>
        <div class="h-50"></div> 
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