<template>
    <div class="rounded-lg" style="box-shadow: 0 0 10px 5px rgba(255, 255, 255, 0.5);">
      <div class="defaultcard rounded-lg shadow-lg transition-all duration-200 transform hover:shadow-2xl hover:-translate-y-2">
        <div class="p-4">
          <h2 class="text-lg mb-3">
            <slot name="id">
              <div class="flex gap-4 justify-between" :alt="props.number">
                <p>{{ props.id }}</p>
                <div style="font-size: xx-small;">
                  <p>{{ props.time }}</p>
                  <p :alt="props.index">层数：{{ props.index }}</p>
                </div>
              </div>
            </slot>
          </h2>
          <h3 v-if="props.reply" class="text-lg mb-4 bg-pink-100 p-2 rounded">
            <slot name="reply">
              <div class="flex gap-2 items-center">
                <p class="font-semibold">回复 >></p>
                <p class="text-black">{{ props.reply }}</p>
              </div>
            </slot>
          </h3>
          <p class="mb-3">
            <slot name="content">
              <p>{{ props.content }}</p>
            </slot>
          </p>
          <div v-if="props.imageUrls && props.imageUrls.length > 0" class="mb-3 flex flex-wrap gap-3">
            <img 
                v-for="(relativePath, imgIndex) in props.imageUrls" 
                :key="imgIndex" 
                :src="`${IMAGE_BASE_URL}${relativePath}`" 
                :alt="`Image ${imgIndex + 1}`" 
                class="h-32 w-32 object-cover rounded border border-gray-300 cursor-pointer shadow-md hover:shadow-lg transition-shadow"
                @click.stop="openImageModal(`${IMAGE_BASE_URL}${relativePath}`)" 
            />
          </div>
          <div class="flex justify-end items-center gap-2">
            <slot name="end">
              <div class="card flex">
                <ToggleButton
                v-model="checked"
                off-icon="pi pi-thumbs-up"
                on-icon="pi pi-thumbs-up-fill"
                class="w-20"
                aria-label="点赞操作" 
                :off-label="likeCount.toString()"
                :on-label="likeCount.toString()"
                @change="handleThumbsToggle"/>
              </div>
              <Button :alt="props.index" @click="refresh" variant="outlined" raised style="font-size: 10px;" class="text w-18 h-8" label="回复" icon="pi pi-reply" />
            </slot>
          </div>
        </div>
      </div>
    </div>

    <Dialog v-model:visible="isImageModalVisible" modal header="图片预览" :style="{ width: '90vw', maxWidth: '1000px' }">
        <img :src="currentModalImageUrl" alt="Full image preview" class="w-full h-auto max-h-[85vh] object-contain" />
    </Dialog>
  </template>
  
  <script lang="ts" setup>
import Button from 'primevue/button';
import 'primeicons/primeicons.css';
import ToggleButton from 'primevue/togglebutton';
import Dialog from 'primevue/dialog';
import { useDialogStore } from '../stores/dialog';
import { onMounted,ref, defineProps } from 'vue';
import {toggleLike} from '../utils/like';
import axiosInstance from '../utils/likestatus';

const IMAGE_BASE_URL = 'https://localhost/i/';

const dialog = useDialogStore();
const checked = ref(false);

const isImageModalVisible = ref(false);
const currentModalImageUrl = ref('');

function refresh() {
  dialog.Dialogvisible = true;
  dialog.replyuser = props.id;
}

const props = defineProps<{
  id: string;
  reply?: string;
  content: string;
  index: number | string;
  thumbs: number | string;
  time: string;
  number: number | string;
  number_primary:string;
  imageUrls?: string[];
}>();
const likeCount = ref(Number(props.thumbs))

const openImageModal = (imageUrl: string) => {
    currentModalImageUrl.value = imageUrl;
    isImageModalVisible.value = true;
};

const handleThumbsToggle=async()=>{
    const isNowChecked = checked.value
    console.log( isNowChecked)
  try {
    await toggleLike({
    reply_id: String(props.number_primary),
    action: isNowChecked ? 'like' : 'unlike'
    })
    likeCount.value += isNowChecked ? 1 : -1
    console.log(isNowChecked ? '点赞成功' : '取消点赞成功')
    
  } catch (error) {
    console.error('点赞操作失败:', error)
    checked.value = !checked.value
  }
}
const checkLikeStatus = async () => {
  try {
    const response = await axiosInstance.get('/like-status', {
      params: { reply_id: props.number_primary }
    });
    checked.value = response.data.liked;
  } catch (error) {
    console.error('获取点赞状态失败:', error);
  }
};

onMounted(() => {
  checkLikeStatus();
});
</script>
  
  <style scoped>
  .defaultcard {
    cursor: url('../assets/ani/select_2.png'), pointer;
  }
  </style>
  