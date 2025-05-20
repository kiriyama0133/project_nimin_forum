<script setup lang="ts">
import subcltureheader from '@/components/Headers/subcltureheader.vue';
import defaultcard from '@/components/Cards/defaultcard.vue';
import axiosInstance from '@/utils/getCards'
import axiosInstance_upload from '@/utils/upload'
import {useCarddata} from '@/stores/carddata'
import { ref } from 'vue';
import { isloading } from '@/stores/isloading';
import type { SendTopic } from '@/types/sendTopic';
import { useCounterStore } from '@/stores/login_register';
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
const selectedFiles = ref<File[]>([]);
const fileInputRef = ref<HTMLInputElement | null>(null); // Ref for file input element
const imagePreviewUrls = ref<string[]>([]);
const isUploading = ref(false);
const uploadProgress = ref(0);

// --- Function to open the dialog ---
const openTopicDialog = () => {
    // Check if username is available
    if (!userStore.userInfo.username) {
        toast.add({ severity: 'warn', summary: '请登录和申请饼干', detail: '请先登录或确保用户信息已加载。', life: 3000 });
        return;
    }
    topicText.value = '';
    removeSelectedImage();
    isDialogVisible.value = true;
};
// --- Function to trigger hidden file input ---
const triggerFileInput = () => {
    fileInputRef.value?.click();
};

// --- 提交图片资源的函数 ---
const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const files = target.files;

    if (!files || files.length === 0) {
        removeSelectedImage(); // Clear if no files selected
        return;
    }

    // Clear previous selections
    selectedFiles.value = [];
    imagePreviewUrls.value = [];

    let filesToProcess = Array.from(files); // Convert FileList to Array

    if (filesToProcess.length > 3) {
        toast.add({ severity: 'warn', summary: '提示', detail: '最多只能选择3张图片。已选择前3张。', life: 3000 });
        filesToProcess = filesToProcess.slice(0, 3); // Take only the first 3
    }

    for (const file of filesToProcess) {
        if (file && file.type.startsWith('image/')) {
            selectedFiles.value.push(file);
            // Create image preview
            const reader = new FileReader();
            reader.onload = (e) => {
                if (e.target?.result) {
                    imagePreviewUrls.value.push(e.target.result as string);
                }
            };
            reader.onerror = (e) => {
                console.error("FileReader 错误:", e);
                // Optionally remove the corresponding file from selectedFiles if preview fails for one
            }
            reader.readAsDataURL(file);
        } else {
            toast.add({ severity: 'warn', summary: '文件类型错误', detail: `文件 "${file.name}" 不是有效的图片格式，已忽略。`, life: 3000 });
        }
    }
    // Reset file input value to allow re-selecting the same file(s) if needed after removal
    if (fileInputRef.value) {
        fileInputRef.value.value = '';
    }
};

// --- Function to remove selected image ---
const removeSelectedImage = () => {
    selectedFiles.value = [];
    imagePreviewUrls.value = [];
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


const handleSendTopic = async () => {

    if (!topicText.value.trim() && selectedFiles.value.length === 0) {
        toast.add({ severity: 'warn', summary: '提示', detail: '请输入内容或选择至少一张图片！', life: 3000 });
        return;
    }
    // --------------------上传图片部分-------------------------
    if (selectedFiles.value.length > 0) { // 选中的上传的图片
        isUploading.value = true;
        uploadProgress.value = 0;

        const formData = new FormData();
        // 创建一个提交的表
        for (const file of selectedFiles.value) {
            // 遍历提交的文件
            formData.append('imageFiles', file);
        }
        try {
            console.log(`开始上传 ${selectedFiles.value.length} 张图片...`);
            // 下面是对应的接口的实现
            const imageResponse = await axiosInstance_upload.post('/upload-images', formData, {
                onUploadProgress: (progressEvent) => {
                    // 计算百分比
                    if (progressEvent.total) {
                        uploadProgress.value = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    }
                }
            });

            // 后端返回Message = "上传成功"
            if (imageResponse.data && imageResponse.data.message) {
                // 上传完成的代码
                console.log("所有图片处理阶段完成，服务端消息:", imageResponse.data.message);
                console.log(imageResponse.data.data)
                toast.add({ severity: 'success', summary: '图片处理成功', detail: imageResponse.data.message, life: 3000 });
            } else {
                 // 错误处理
                 console.error("图片上传响应格式不符合预期或未包含message:", imageResponse.data);
                 toast.add({ severity: 'error', summary: '上传响应错误', detail: '图片上传后服务器响应异常。话题未发送。', life: 4000 });
                 isUploading.value = false;
                 uploadProgress.value = 0;
                 return; // Stop if batch upload response is not right
            }
            console.log()
            uploadProgress.value = 0;

            const currentTime = getCurrentTimeFormatted();

            // 发送话题卡片的部分
            const cardData: SendTopic = {
                id: userStore.userInfo.username || '',
                content: topicText.value,
                time: currentTime,
                category: cardstore.category,
                imageUrls: imageResponse?.data?.data || []
            };

            console.log("准备发送话题:", cardData);

            isUploading.value = true; 
            uploadProgress.value = 0; 

            try {
                const response = await axiosInstance.post('/addcard', cardData);
                console.log("发送成功:", response.data);
                refresh('/subculture', '/getcard', cardstore.category);
                toast.add({ severity: 'success', summary: '成功', detail: response.data.message || '发送成功！', life: 3000 });
                topicText.value = '';
                removeSelectedImage(); // MODIFIED: Clear multiple files
                isDialogVisible.value = false;

            } 
            catch (error: any) 
            {
                console.error("发送失败:", error);
                const errorMessage = error.response?.data?.detail || error.response?.data?.message || '发送失败，请稍后重试';
                toast.add({ severity: 'error', summary: '错误', detail: errorMessage, life: 4000 });
            } 
            finally 
            {
                isUploading.value = false; // Finish loading indication
                uploadProgress.value = 0;
            }

        } 
        catch (uploadError: any) {
            console.error("图片批量上传失败:", uploadError);
            const uploadErrorMessage = uploadError.response?.data?.message || `图片上传失败 (${selectedFiles.value.length}张)，话题未发送。`;
            toast.add({ severity: 'error', summary: '图片上传错误', detail: uploadErrorMessage, life: 4000 });
            isUploading.value = false;
            uploadProgress.value = 0;
            return; 
        }
    } else { // <-- This is the new else block
        // Logic to send topic when no images are selected
        isUploading.value = true; // Indicate loading
        const currentTime = getCurrentTimeFormatted();
        const cardData: SendTopic = {
            id: userStore.userInfo.username || '',
            content: topicText.value,
            time: currentTime,
            category: cardstore.category,
            imageUrls: [] // No images
        };

        console.log("准备发送无图片的话题:", cardData);

        try {
            const response = await axiosInstance.post('/addcard', cardData);
            console.log("发送成功:", response.data);
            refresh('/subculture', '/getcard', cardstore.category);
            toast.add({ severity: 'success', summary: '成功', detail: response.data.message || '发送成功！', life: 3000 });
            topicText.value = '';
            // removeSelectedImage(); // No images to remove
            isDialogVisible.value = false;
        } catch (error: any) {
            console.error("发送失败:", error);
            const errorMessage = error.response?.data?.detail || error.response?.data?.message || '发送失败，请稍后重试';
            toast.add({ severity: 'error', summary: '错误', detail: errorMessage, life: 4000 });
        } finally {
            isUploading.value = false;
            uploadProgress.value = 0;
        }
    }
};

//刷新卡片
function refresh(path: string, api: string, category: string) {
    console.log(`刷新分类: ${category}, 路径: ${path}, API: ${api}`);
    cardstore.carddata.splice(0, cardstore.carddata.length); // 清空列表
    isloadingstore.dataloading = true; // This can remain if used for other global state
    dataloading.value = true; // Controls the spinner
    cardstore.category = category;//设置分类
    //console.log("当前的分类是：",cardstore.category)
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
            // Handle case where category might have no cards initially
        }
    }).catch(error => {
        console.error(`从 ${api} (分类: ${category}) 刷新初始数据失败:`, error);
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
                :imageUrls="item.imageUrls"
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
                    <label class="block mb-2 text-sm font-medium text-gray-700">上传图片 (最多3张)</label>
                    <input
                        ref="fileInputRef"
                        type="file"
                        id="topic-image-hidden"
                        accept="image/*"
                        multiple
                        @change="handleFileChange"
                        class="hidden" />
                    <Button
                        label="选择图片"
                        icon="pi pi-image"
                        severity="secondary"
                        outlined
                        :disabled="isUploading || selectedFiles.length >= 3"
                        @click="triggerFileInput" />

                    <div v-if="imagePreviewUrls.length > 0" class="mt-3 flex flex-wrap gap-2">
                         <div v-for="(previewUrl, index) in imagePreviewUrls" :key="index" class="relative inline-block">
                             <img :src="previewUrl" :alt="'Image preview ' + (index + 1)" class="h-24 w-24 object-cover rounded border border-gray-300" />
                         </div>
                    </div>
                    <Button v-if="selectedFiles.length > 0" 
                            label="移除所有图片" 
                            icon="pi pi-times" 
                            @click="removeSelectedImage" 
                            :disabled="isUploading"
                            severity="danger"
                            text
                            size="small"
                            class="mt-2" />
                     <p v-if="selectedFiles.length > 0 && imagePreviewUrls.length < selectedFiles.length" class="mt-1 text-sm text-gray-500">正在加载预览...</p>
                </div>

                <div v-if="isUploading" class="mt-2">
                    <ProgressBar :value="uploadProgress"></ProgressBar>
                    <p class="text-sm text-center mt-1">正在上传... {{ uploadProgress }}%</p>
                </div>
             </div>

             <template #footer>
                <Button label="取消" icon="pi pi-times" @click="isDialogVisible = false" severity="secondary" outlined :disabled="isUploading"></Button>
                <Button label="发送" icon="pi pi-send" @click="handleSendTopic" :disabled="(!topicText.trim() && selectedFiles.length === 0) || isUploading" :loading="isUploading"></Button>
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