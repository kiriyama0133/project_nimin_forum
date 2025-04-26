<script lang="ts" setup>
import sendcard from '../components/sendcard.vue';
import { ElMessage } from 'element-plus'
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import {useDialogStore} from '../stores/dialog'
import axiosInstance from '../utils/getReply'
import {useCarddata} from '../stores/contentsotre.ts'
import { onMounted, ref } from 'vue';
const dialog = useDialogStore();
const sendcardstore = useCarddata()
let dataend = ref(false);
let dataloading = ref(false);
let click_reply = ref(false) //点击回复按钮的标志
const open1 = () => {
  ElMessage({
    message: '回复成功！😊',
    type: 'success',
    plain: true,
  })
}
//发送按钮的函数
function send(){
  click_reply.value = true
  setTimeout(() => {
    dialog.Dialogvisible = false
    click_reply.value = false
    open1()
  }, 2000);
}
//回复模块的数据示例
const submitregister = async () => {
  dataloading.value = true; // 开始加载
  try {
    const response = await axiosInstance.get('/getsendCard');
    console.log('Registration Successful:', response);
    sendcardstore.contentdata.push(response.data);
    console.log('目前已得到的卡片数据：', sendcardstore.contentdata);
  } catch (error) {
    console.error('请求失败:', error);
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
  if (scrollTop + clientHeight >= scrollHeight) {
    onScrollToBottom();
  }
};
/*let carddata_: sendcarddata[] = [
    {
    id:"Kiriyama",
    content:"你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面",
    thumbs:0
    },
    {
    id:"KJHKJHJ",
    reply:"Kiriyama",
    content:"你好，这里是一条回复，回复内容会被加以粉色装饰",
    thumbs:0
    },
    {
    id:"Kiriyama",
    content:"你好",
    thumbs:0
    },
    {
    id:"Kiriyama",
    content:"你好",
    thumbs:0
    },   
]*/
</script>
<template>
  <div @scroll="handleScroll"
  ref="scrollContainer" class="subculture scroll-custom h-full overflow-y-auto">

  <div class="card flex justify-center">
        <Dialog v-model:visible="dialog.Dialogvisible" modal header="回复" :style="{ width: '25rem' }">
            <div class="flex items-center gap-4 mb-4">
                <label for="username" class="font-semibold w-24">回复的用户</label>
                <p>{{ dialog.replyuser }}</p>
            </div>
            <div class="flex items-center gap-4 mb-8">
                <InputText id="email" class="flex-auto" autocomplete="off"></InputText>   
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
    <div class="flex flex-col gap-1 p-2">
        <sendcard v-for="(item,i) in sendcardstore.contentdata"
            :number="item.number"
            :id="item.id"
            :index="i+1"
            :reply="item.reply"
            :time = "item.time"
            :content="item.content"
            :thumbs="item.thumbs"
        >
    </sendcard>
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