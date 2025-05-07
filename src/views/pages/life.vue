<script setup lang="ts">
import subcltureheader from '../../components/subcltureheader.vue';
import defaultcard from '../../components/defaultcard.vue';
import axiosInstance from '../../utils/getCards'
import {useCarddata} from '../../stores/carddata'
import { ref } from 'vue';
import { isloading } from '../../stores/isloading';
import type { SendTopic } from '../../types/sendTopic';
import { useCounterStore } from '../../stores/login_register';
// Import PrimeVue components
import Dialog from 'primevue/dialog';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import FloatLabel from 'primevue/floatlabel';
import ProgressBar from 'primevue/progressbar';
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
const selectedFile = ref<File | null>(null);
const fileInputRef = ref<HTMLInputElement | null>(null); // Ref for file input element
const imagePreviewUrl = ref<string | null>(null);
const isUploading = ref(false);
const uploadProgress = ref(0);

// --- Function to open the dialog ---
const openTopicDialog = () => {
    topicText.value = '';
    removeSelectedImage();
    isDialogVisible.value = true;
};

// --- Function to trigger hidden file input ---
const triggerFileInput = () => {
    fileInputRef.value?.click();
};

// --- Function to handle file selection and create preview ---
const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0];

    if (file && file.type.startsWith('image/')) {
        selectedFile.value = file;
        console.log("选择的文件:", selectedFile.value.name);

        // Create image preview
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreviewUrl.value = e.target?.result as string;
        };
        reader.onerror = (e) => {
            console.error("FileReader 错误:", e);
            imagePreviewUrl.value = null; // Clear preview on error
        }
        reader.readAsDataURL(file);
    } else {
        console.log("未选择文件或文件不是图片。");
        removeSelectedImage(); // Clear if selection is invalid or cancelled
    }
};

// --- Function to remove selected image ---
const removeSelectedImage = () => {
    selectedFile.value = null;
    imagePreviewUrl.value = null;
    if (fileInputRef.value) {
        fileInputRef.value.value = ''; // Clear the file input
    }
};

// --- Function to get current time in YYYY-MM-DD-HH:MM format ---
const getCurrentTimeFormatted = (): string => {
    const now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0'); // Months are 0-indexed
    const day = now.getDate().toString().padStart(2, '0');
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    return `${year}-${month}-${day}-${hours}:${minutes}`;
};

// --- Function to handle sending the topic ---
const handleSendTopic = async () => {
    if (!topicText.value.trim()) { // Image part removed for now
        toast.add({ severity: 'warn', summary: '提示', detail: '请输入内容！', life: 3000 });
        return;
    }
    const currentTime = getCurrentTimeFormatted();
    const cardData: SendTopic = {
        id: userStore.userInfo.username || '',
        content: topicText.value,
        time: currentTime,
        category: cardstore.category
    };

    console.log("准备发送话题:", cardData);

    isUploading.value = true; // Use isUploading as a general loading indicator here
    uploadProgress.value = 0; // Reset progress (though not used for text-only)

    try {
      const response = await axiosInstance.post('/addcard', cardData); // Send data
      console.log("发送成功:", response.data);
      refresh('/subculture', '/getcard', cardstore.category);
      //发送成功后，从服务端获取
      toast.add({ severity: 'success', summary: '成功', detail: response.data.message || '发送成功！', life: 3000 });

      // --- TODO: Optionally refresh the card list after successful post ---
      // E.g., call a function to reload the first page or insert the new card optimistically
      // loadInitialData(); // Reloads everything, might not be ideal

      // Reset form and close dialog on success
      topicText.value = '';
      // removeSelectedImage(); // Keep if you re-add image logic
      isDialogVisible.value = false;

    } catch (error: any) {
      console.error("发送失败:", error);
      const errorMessage = error.response?.data?.detail || error.response?.data?.message || '发送失败，请稍后重试';
      toast.add({ severity: 'error', summary: '错误', detail: errorMessage, life: 4000 });
    } finally {
      isUploading.value = false; // Finish loading indication
      uploadProgress.value = 0;
    }
};

//刷新卡片
function refresh(path: string, api: string, category: string) {
    console.log(`刷新分类: ${category}, 路径: ${path}, API: ${api}`);
    cardstore.carddata.splice(0, cardstore.carddata.length); // 清空列表
    isloadingstore.dataloading = true;
    cardstore.category = category;//设置分类
    //console.log("当前的分类是：",cardstore.category)
    isloadingstore.dataend = false;
    //第一次加载内容
    axiosInstance.post(api, { skip: 0, category: category }).then((response) => {
        const receivedCards = response.data.data;
        if (receivedCards && Array.isArray(receivedCards)) {
            cardstore.carddata.push(...receivedCards);
            console.log(`分类 "${category}" 的初始卡片数据已加载:`, cardstore.carddata);
            if (cardstore.carddata.length === 0) {
                isloadingstore.dataend = true;
            }
        } else {
            console.warn(`分类 "${category}" 返回的初始卡片数据无效或为空:`, receivedCards);
            // Handle case where category might have no cards initially
        }
    }).catch(error => {
        console.error(`从 ${api} (分类: ${category}) 刷新初始数据失败:`, error);
        toast.add({ severity: "error", summary: "错误", detail: "加载初始数据失败", life: 3000 });
    }).finally(() => {
        // cardstore.initialLoading = false; // Reset loading state if used
    });
}
//发送请求获得前5个卡片数据
const submitregister = async () => {
  dataloading.value = true; // 开始加载
  try {
    const currentItemCount = cardstore.carddata.length;
    console.log(`请求下一页，跳过: ${currentItemCount}`);

    const response = await axiosInstance.post('/getcard', { skip: currentItemCount,category:cardstore.category });
    const receivedCards = response.data.data;

    if (receivedCards && Array.isArray(receivedCards)) {
      cardstore.carddata.push(...receivedCards);
      console.log('已添加数据：', receivedCards);
      console.log('目前总卡片数据：', cardstore.carddata);
            if (receivedCards.length < 5) {
                console.log("分类",cardstore.category,"的卡片数据不足5条，已设置为已结束。")
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
//   console.log('滚动位置：', scrollTop);
//   console.log('容器高度：', clientHeight);
//   console.log('容器总高度：', scrollHeight);
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
            @click="openTopicDialog"
            title="发送话题"
            class="fixed bottom-5 right-5 w-10 h-10 bg-black text-white rounded-full shadow-lg
                   flex items-center justify-center
                   hover:bg-gray-700 transition-colors duration-200 z-20">
            <i class="pi pi-send text-xl"></i>
        </button>

        <Dialog v-model:visible="isDialogVisible" modal header="发送新话题" :style="{ width: '90vw', maxWidth: '500px' }">
             <div class="flex flex-col gap-4 mt-4 pt-4">
                <FloatLabel>
                    <Textarea v-model="topicText" id="topic-text" :disabled="isUploading" class="w-full resize-none" rows="5" />
                    <label for="topic-text">说点什么吧...</label>
                </FloatLabel>

                <div>
                    <label class="block mb-2 text-sm font-medium text-gray-700">上传图片 (可选)</label>
                    <input
                        ref="fileInputRef"
                        type="file"
                        id="topic-image-hidden"
                        accept="image/*"
                        @change="handleFileChange"
                        class="hidden" />
                    <Button
                        label="选择图片"
                        icon="pi pi-image"
                        severity="secondary"
                        outlined
                        :disabled="isUploading"
                        @click="triggerFileInput" />

                    <div v-if="imagePreviewUrl" class="mt-3 relative inline-block">
                         <img :src="imagePreviewUrl" alt="Image preview" class="max-w-full h-auto max-h-40 rounded border border-gray-300" />
                         <button @click="removeSelectedImage" :disabled="isUploading" class="absolute top-0 right-0 -mt-2 -mr-2 bg-red-500 text-white rounded-full p-1 leading-none hover:bg-red-600 focus:outline-none" title="移除图片">
                             <i class="pi pi-times text-xs"></i>
                         </button>
                    </div>
                     <p v-if="selectedFile && !imagePreviewUrl" class="mt-1 text-sm text-gray-500">正在加载预览...</p>
                </div>

                <div v-if="isUploading" class="mt-2">
                    <ProgressBar :value="uploadProgress"></ProgressBar>
                    <p class="text-sm text-center mt-1">正在上传... {{ uploadProgress }}%</p>
                </div>
             </div>

             <template #footer>
                <Button label="取消" icon="pi pi-times" @click="isDialogVisible = false" severity="secondary" outlined :disabled="isUploading"></Button>
                <Button label="发送" icon="pi pi-send" @click="handleSendTopic" :disabled="(!topicText.trim() && !selectedFile) || isUploading" :loading="isUploading"></Button>
             </template>
        </Dialog>
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