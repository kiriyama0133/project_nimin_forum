<template>
<div class="rounded-lg">
    <div class="defaultcard bg-gray-300 rounded-lg shadow-lg transition-all 
        duration-500 transform hover:shadow-2xl hover:-translate-y-2">
        <div @click="gotoreply" class="p-4">
            <h2 class="text-lg text-gray-800 mb-4">
                <slot name="title">
                    <div class="flex gap-4 justify-between">
                        <div>
                            <p class="Mate">No.{{ props.number }}，分区：{{ props.category }}</p>
                            <p class="User_Id">{{ props.id }}</p>
                        </div>
                        <p class="Mate" style="font-size: xx-small;">{{ props.time }}</p>
                    </div>
                </slot>
            </h2>
            <!-- 添加回复显示区域 -->
            <h3 v-if="props.reply" class="text-lg mb-4 bg-pink-100 p-2 rounded">
                <slot name="reply">
                    <div class="flex gap-2 items-center">
                        <p class="Reply_text">回复 >>{{ props.reply }}</p>
                    </div>
                </slot>
            </h3>
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
    </div>
</div>

<Dialog v-model:visible="isImageModalVisible" modal header="图片预览" :style="{ width: '90vw', maxWidth: '800px' }">
    <img :src="currentModalImageUrl" alt="Full image preview" class="w-full h-auto max-h-[80vh] object-contain" />
</Dialog>
</template>

<script lang="ts" setup>
const props = defineProps<{ 
    number: string | number;
    id: string;
    content: string;
    time: string;
    thumbs?: string | number;
    imageUrls?: string[];
    reply?: string;
    number_primary?: string;
    category?: string;
}>();

import { useRouter } from 'vue-router';
import 'primeicons/primeicons.css'
import Dialog from 'primevue/dialog';
import { ref } from 'vue'
const IMAGE_BASE_URL = import.meta.env.VITE_API_URL + '/i/';
const router = useRouter()
const isImageModalVisible = ref(false);
const currentModalImageUrl = ref('');

const gotoreply = () => {
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

</script>

<style scoped>
.defaultcard {
    cursor: url('@/assets/ani/link_2.png'), pointer;
}
.Mate {
    font-weight: inherit;
    transition: color 0.2s ease;
}
.content-text {
    font-weight: inherit;
    transition: color 0.2s ease;
    white-space: pre-wrap;
    word-wrap: break-word;
    word-break: break-word;
    overflow-wrap: break-word;
}
.User_Id {
    font-weight: inherit;
    transition: color 0.2s ease;
}
.Reply_text {
    font-weight: inherit;
    transition: color 0.2s ease;
}
</style>
