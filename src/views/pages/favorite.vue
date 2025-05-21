<script setup lang="ts">
import subcltureheader from '@/components/Headers/subcltureheader.vue';
import defaultcard from '@/components/Cards/defaultcard.vue';
import axiosInstance from '@/utils/getCards'
import {useCarddata} from '@/stores/carddata'
import { ref,onMounted } from 'vue';
import { isloading } from '@/stores/isloading';
import { useCounterStore } from '@/stores/login_register';
// Import PrimeVue components

// Import PrimeIcons if not globally available
import 'primeicons/primeicons.css';

// Import useToast if not already (assuming you use PrimeVue Toast)
import { useToast } from "primevue/usetoast";
const toast = useToast(); // Initialize toast
const isloadingstore = isloading();
const cardstore = useCarddata();
let dataloading = ref(false);
const userStore = useCounterStore();
// --- State for New Topic Dialog ---
const isDialogVisible = ref(false);
const topicText = ref('');
// --- Function to open the dialog ---
const openTopicDialog = () => {
    // Check if username is available
    if (!userStore.userInfo.username) {
        toast.add({ severity: 'warn', summary: '请登录和申请饼干', detail: '请先登录或确保用户信息已加载。', life: 3000 });
        return;
    }
    topicText.value = '';
    isDialogVisible.value = true;
};

// --- Function to trigger hidden file input ---

// --- 提交图片资源的函数 ---


        

//刷新卡片
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
//发送请求获得前5个卡片数据
const submitregister = async () => {
  dataloading.value = true; // 开始加载
  try {
    const currentItemCount = cardstore.carddata.length;
    console.log(`请求下一页，跳过: ${currentItemCount}`);
    const response = await axiosInstance.post('/getfavoritecard', { skip: currentItemCount});
    const receivedCards = response.data.data;
    console.log("收到的数据",receivedCards)
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
    dataloading.value = false; // 加载完成
  }
};

// 滚动事件处理函数
const scrollContainer = ref<HTMLElement | null>(null); // 定义模板引用
const handleScroll = () => {
  if (!scrollContainer.value) return; // 确保引用存在
  const scrollTop = scrollContainer.value.scrollTop;
  const clientHeight = scrollContainer.value.clientHeight;
  const scrollHeight = scrollContainer.value.scrollHeight;
  // 判断是否滚动到底部
  if (scrollTop + clientHeight >= scrollHeight - 10) { // Trigger closer to bottom
    onScrollToBottom();
  }
};

const onScrollToBottom = () => {
  // 如果数据已结束或已在加载，则阻止获取
  if (isloadingstore.dataend || dataloading.value) {
    return;
  }
  console.log("滚动到底部了！准备延时加载...");

  // 设置 dataloading 为 true *之前* 启动延时，以显示加载指示器
  dataloading.value = true;

  // 延时1秒 (1000毫秒) 后执行数据请求
  setTimeout(() => {
    // 在延时结束后，再次检查是否仍在加载中（防止快速滚动触发多次延时）
    // 并且检查数据是否已经结束（虽然不太可能在此期间改变，但以防万一）
    if (dataloading.value && !isloadingstore.dataend) {
        console.log("延时结束，开始获取下一页数据...");
        submitregister(); // 获取下一页
        // 注意：submitregister 内部会设置 dataloading = false in finally
    } else {
        console.log("延时期间加载状态改变，取消本次数据获取。");
        // 如果延时期间状态改变，确保重置加载状态（如果submitregister没运行）
        if (dataloading.value) dataloading.value = false;
    }
  }, 1000); 
};
onMounted(() => {
  cardstore.carddata.splice(0, cardstore.carddata.length);
  refresh('/favorite', '/getfavoritecard');
});
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
                :imageUrls="item.imageUrls"
            >
            </defaultcard>
        </div>

        <div v-if="cardstore.carddata.length === 0 && !dataloading && isloadingstore.dataend" class="text-center p-5 text-gray-500">
            还没有收藏的内容哦~
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