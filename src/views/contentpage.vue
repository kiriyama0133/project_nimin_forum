<script lang="ts" setup>
import sendcard from '../components/sendcard.vue';
import { ElMessage } from 'element-plus'
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import Textarea from 'primevue/textarea';
import {useDialogStore} from '../stores/dialog'
import axiosInstance from '../utils/getCards'
import {useCarddata} from '../stores/contentsotre.ts'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { AddReplyCardClient,ReplyCardRequest,AddReplyCardResponse } from '../types/sendcard';
import { getCurrentTimeFormatted } from '../utils/getCurrentTimeFormate';
import { useCounterStore } from '../stores/login_register';
import { getOneCard } from '../utils/getCards';
import type { carddata } from '../types/carddata';
const starter =ref<carddata|null>(null)
const dialog = useDialogStore();
const sendcardstore = useCarddata()
const route = useRoute();
const userStore = useCounterStore();
let dataend = ref(false);
let dataloading = ref(false);
let click_reply = ref(false) //点击回复按钮的标志
const replyContent = ref(''); // Ref for the reply input in the dialog

// --- Function to open dialog for a direct reply to the post ---
const openDirectReplyDialog = () => {
  dialog.replyuser = ''; // Clear any specific user being replied to
  replyContent.value = ''; // Clear previous reply text
  dialog.Dialogvisible = true;
};

//成功信息提示
const open1 = () => {
  ElMessage({
    message: '回复成功！😊',
    type: 'success',
    plain: true,
  })
}

//错误信息提示
const open_error = (message: string) => {
  ElMessage({
    message: message + '😥',
    type: 'error',
    plain: true,
  })
}

//发送按钮的函数
async function send(){
  if (!replyContent.value.trim()) {
    open_error('回复内容不能为空！');
    return;
  }

  click_reply.value = true;

  const originalPostNumberStr = route.query.number as string;
  if (!originalPostNumberStr) {
      open_error('无效的帖子编号。');
      click_reply.value = false;
      return;
  }
  const originalPostNumber = parseInt(originalPostNumberStr);
   if (isNaN(originalPostNumber)) {
      open_error('帖子编号格式错误。');
      click_reply.value = false;
      return;
  }

  setTimeout(async () => {
    const replyData: AddReplyCardClient = {
      number: originalPostNumber,
      id: userStore.userInfo.username || '', //回复用户用的名称，后期加入cookie去替代
      content: replyContent.value,
      time: getCurrentTimeFormatted(),
      reply: dialog.replyuser || undefined, // 回复的用户
    };

    try {
      console.log('Sending reply:', replyData);
      const response = await axiosInstance.post('/addreplycard', replyData);
      console.log('Reply sent successfully:', response.data);
      // The line below implements the refresh
      
      dialog.Dialogvisible = false;
      replyContent.value = ''; // 回复的内容
      open1(); // Shows success message
      fetchReplies(true); // Fetches the first page of replies
    } catch (error: any) {
      console.error('Failed to send reply:', error);
      const errorMessage = error.response?.data?.detail || error.response?.data?.message || '回复失败，请稍后再试';
      open_error(errorMessage);
    } finally {
      click_reply.value = false;
    }
  }, 1000);
}

// --- Function to fetch replies for the current post ---
const fetchReplies = async (isInitialLoad = false) => {
  if (dataloading.value || dataend.value && !isInitialLoad) return; // Don't fetch if already loading or all data loaded (unless initial)

  dataloading.value = true;
  const postNumberStr = route.query.number as string;
  if (!postNumberStr) {
    console.error('Post number is missing from route query.');
    open_error('无法加载回复：帖子编号缺失。');
    dataloading.value = false;
    dataend.value = true; // Prevent further loading attempts
    return;
  }
  const postNumber = parseInt(postNumberStr);
  if (isNaN(postNumber)) {
    console.error('Invalid post number in route query:', postNumberStr);
    open_error('无法加载回复：帖子编号格式错误。');
    dataloading.value = false;
    dataend.value = true; // Prevent further loading attempts
    return;
  }

  const requestPayload: ReplyCardRequest = {
    number: postNumber,
    skip: isInitialLoad ? 0 : sendcardstore.contentdata.length
  };

  try {
    console.log('Fetching replies with payload:', requestPayload);
    const response = await axiosInstance.post<AddReplyCardResponse>('/getreplycard', requestPayload);
    
    if (response.data && Array.isArray(response.data.data)) {
      if (isInitialLoad) {
        sendcardstore.contentdata = response.data.data;
        dataend.value = false; // Explicitly reset dataend for initial load
      } else {
        // Only append if there's new data
        if (response.data.data.length > 0) {
            sendcardstore.contentdata.push(...response.data.data);
        }
      }
      console.log('Replies received:', response.data.data);
      console.log('Current total replies:', sendcardstore.contentdata);
      
      // If fewer items than page size (e.g., 5 based on previous logic) are returned, it's the end.
      if (response.data.data.length < 5) { 
        console.log('All replies loaded or last page received (less than page size).');
        dataend.value = true;
      }
      // If isInitialLoad was true and a full page was loaded, dataend is already false.
      // If it was a subsequent load and a full page was loaded, dataend also remains false (unless the above condition met).
    } else {
      console.warn('No data received or data format is incorrect for replies.');
      dataend.value = true; // Assume end if data is not as expected
    }
  } catch (error) {
    console.error('Failed to fetch replies:', error);
    open_error('加载回复失败。');
    // dataend.value = true; // Optionally, set to true to prevent repeated failed attempts on scroll
  } finally {
    dataloading.value = false;
  }
};

onMounted(()=>{
  // Clear previous post's replies and reset flags when component mounts for a new post
  sendcardstore.contentdata = [];
  dataend.value = false;
  dataloading.value = false; // Ensure loading is false before initial fetch
  fetchReplies(true);// Fetch initial replies for the current post
})
onMounted(async()=>{
  const defuatcardnumber =Number(route.query.number)
  if(defuatcardnumber){
    starter.value=await getOneCard(defuatcardnumber)
  }
})
// 滚动事件处理函数
const scrollContainer = ref<HTMLElement | null>(null); // 定义模板引用
const handleScroll = () => {
  if (!scrollContainer.value) return; // 确保引用存在
  const { scrollTop, clientHeight, scrollHeight } = scrollContainer.value;
  // 判断是否滚动到底部
  if (scrollTop + clientHeight >= scrollHeight - 10) { // Trigger a bit before exact bottom
    onScrollToBottom();
  }
};

const onScrollToBottom = () => {
  console.log("滚动到底部了！ attempting to load more replies...");
  // dataloading and dataend checks are handled inside fetchReplies
  fetchReplies(); // Load next page of replies
};

</script>
<template>
  <div @scroll="handleScroll"
  ref="scrollContainer" class="subculture scroll-custom h-full overflow-y-auto relative">
  <div class="flex flex-col gap-1 p-2">
        <sendcard v-if="starter"
            :number="Number(route.query.number) || 0"
            :id="String(starter?.id || '')"
            :time ="String(route.query.time || '')"
            :index="0"
            :content="String(starter?.content || '')"
            :thumbs="Number(starter.thumbs)"
            :number_primary="String(route.query.number)">
        </sendcard>
    </div>
  <div class="card flex justify-center">
        <Dialog v-model:visible="dialog.Dialogvisible" modal header="回复" :style="{ width: '25rem' }">
            <div class="flex items-center gap-4 mb-4">
                <label for="username" class="font-semibold w-24">{{ dialog.replyuser ? '回复用户' : '回复帖子' }}</label>
                <p v-if="dialog.replyuser">{{ dialog.replyuser }}</p>
            </div>
            <div class="flex items-center gap-4 mb-8">
                <Textarea v-model="replyContent" id="replyInput" class="w-full resize-none" rows="5" placeholder="说点什么吧..." />   
            </div>
            <div class="flex justify-end gap-2">
                <Button type="button" label="取消" severity="secondary" @click="dialog.Dialogvisible = false"></Button>
                <Button type="button" label="发送" @click="send">
                    <template v-if="click_reply" #icon>
                        <svg class="animate-spin h-5 w-5" viewBox="0 0 24 24">
                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/>
                            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/>
                        </svg>
                    </template>
                </Button>
            </div>
        </Dialog>
    </div>
    <h2 class="text-lg mb-3">以下是帖No.{{route.query.number}}的回复</h2>
    <div class="flex flex-col gap-1 p-2" v-if="sendcardstore.contentdata.length > 0">
        <sendcard v-for="(item,i) in sendcardstore.contentdata"
            :key="item.id + '-' + i" 
            :number="item.number" 
            :id="item.id"
            :index="i+1"
            :reply="item.reply"
            :time = "item.time"
            :content="item.content"
            :thumbs="item.thumbs"
            :number_primary="item.number_primary"
        >
    </sendcard>
    </div>
    <div v-if="sendcardstore.contentdata.length === 0 && !dataloading && dataend" class="text-center p-4 text-gray-500">
        还没有人回复哦，快来抢沙发吧！
    </div>

    <div v-if="dataend && sendcardstore.contentdata.length > 0" class="h-20 flex justify-center">
            <p>所有回复都已经加载完了~~ </p>
        </div>  
    <div v-if="dataloading" class="flex justify-center h-20 py-4">
                <div class="flex flex-col items-center">
                <div class="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
                <p class="mt-4 text-gray-600">加载中...</p>
            </div>
        </div>
        

    <!-- Floating Action Button to Reply to Post -->
    <button
        @click="openDirectReplyDialog"
        title="回复帖子"
        class="fixed bottom-5 right-5 w-10 h-10 bg-black text-white rounded-full shadow-lg
                flex items-center justify-center
                hover:bg-gray-700 transition-colors duration-200 z-20">
        <i class="pi pi-send text-xl"></i> <!-- Changed icon to pi-send -->
    </button>

    </div>
</template>
<style scoped>
input{
    cursor: url('../assets/ani/text_2.png'), pointer;    
}
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