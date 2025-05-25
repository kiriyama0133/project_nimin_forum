<template>
    <Dialog v-model:visible="isDialogVisible" modal header="发送新话题" :style="{ width: '90vw', maxWidth: '500px' }">
        <div class="flex flex-col gap-4 mt-4 pt-4">
            <FloatLabel>
                <Textarea v-model="topicText" id="topic-text" :disabled="isUploading" class="w-full resize-none" rows="5" @paste="handlePaste" />
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
                        <button 
                            @click="removeImage(index)" 
                            class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center"
                        >
                            ×
                        </button>
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
            <Button label="取消" icon="pi pi-times" @click="closeDialog" severity="secondary" outlined :disabled="isUploading"></Button>
            <Button label="发送" icon="pi pi-send" @click="handleSendTopic" :disabled="(!topicText.trim() && selectedFiles.length === 0) || isUploading" :loading="isUploading"></Button>
        </template>
    </Dialog>
</template>

<script setup lang="ts">
import { ref, watch, onUnmounted } from 'vue';
import Dialog from 'primevue/dialog';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import FloatLabel from 'primevue/floatlabel';
import ProgressBar from 'primevue/progressbar';
import { useToast } from "primevue/usetoast";
import axiosInstance from '@/utils/getCards';
import type { SendTopic } from '@/types/sendTopic';
import { useCounterStore } from '@/stores/login_register';
import { useKeyboardPaste } from '@/composables/useKeyboardPaste'
import { useEventListener } from '@vueuse/core'
import { uploadImages } from '@/utils/upload';

const props = defineProps<{
    modelValue: boolean;
    category: string;
}>();

const emit = defineEmits<{
    (e: 'update:modelValue', value: boolean): void;
    (e: 'topicSent'): void;
}>();

const toast = useToast();
const userStore = useCounterStore();

const isDialogVisible = ref(props.modelValue);
const topicText = ref('');
const selectedFiles = ref<File[]>([]);
const fileInputRef = ref<HTMLInputElement | null>(null);
const imagePreviewUrls = ref<string[]>([]);
const isUploading = ref(false);
const uploadProgress = ref(0);

const { pastedImages, clearImages } = useKeyboardPaste()

// Watch for modelValue changes
watch(() => props.modelValue, (newValue) => {
    isDialogVisible.value = newValue;
});

// Watch for isDialogVisible changes
watch(isDialogVisible, (newValue) => {
    emit('update:modelValue', newValue);
});

const closeDialog = () => {
    isDialogVisible.value = false;
    resetForm();
};

const resetForm = () => {
    topicText.value = '';
    removeSelectedImage();
};

const triggerFileInput = () => {
    fileInputRef.value?.click();
};

const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const files = target.files;

    if (!files || files.length === 0) {
        removeSelectedImage();
        return;
    }

    selectedFiles.value = [];
    imagePreviewUrls.value = [];

    let filesToProcess = Array.from(files);

    if (filesToProcess.length > 3) {
        toast.add({ severity: 'warn', summary: '提示', detail: '最多只能选择3张图片。已选择前3张。', life: 3000 });
        filesToProcess = filesToProcess.slice(0, 3);
    }

    for (const file of filesToProcess) {
        if (file && file.type.startsWith('image/')) {
            selectedFiles.value.push(file);
            const reader = new FileReader();
            reader.onload = (e) => {
                if (e.target?.result) {
                    imagePreviewUrls.value.push(e.target.result as string);
                }
            };
            reader.onerror = (e) => {
                console.error("FileReader 错误:", e);
            }
            reader.readAsDataURL(file);
        } else {
            toast.add({ severity: 'warn', summary: '文件类型错误', detail: `文件 "${file.name}" 不是有效的图片格式，已忽略。`, life: 3000 });
        }
    }

    if (fileInputRef.value) {
        fileInputRef.value.value = '';
    }
};

const removeSelectedImage = () => {
    selectedFiles.value = [];
    imagePreviewUrls.value = [];
    if (fileInputRef.value) {
        fileInputRef.value.value = '';
    }
};

const getCurrentTimeFormatted = (): string => {
    const now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
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

    if (selectedFiles.value.length > 0) {
        await handleImageUpload();
    } else {
        await sendTopicWithoutImages();
    }
};

const handleImageUpload = async () => {
    isUploading.value = true;
    uploadProgress.value = 0;

    try {
        const imageUrls = await uploadImages(selectedFiles.value);
        toast.add({ severity: 'success', summary: '图片处理成功', detail: '图片上传成功', life: 3000 });
        await sendTopicWithImages(imageUrls);
    } catch (error: any) {
        handleUploadError(error);
        // Reset upload state
        isUploading.value = false;
        uploadProgress.value = 0;
        return; // Prevent sending topic when image upload fails
    }
};

const sendTopicWithImages = async (imageUrls: string[]) => {
    const currentTime = getCurrentTimeFormatted();
    const cardData: SendTopic = {
        id: userStore.userInfo.username || '',
        content: topicText.value,
        time: currentTime,
        category: props.category,
        imageUrls: imageUrls
    };

    await sendTopic(cardData);
};

const sendTopicWithoutImages = async () => {
    const currentTime = getCurrentTimeFormatted();
    const cardData: SendTopic = {
        id: userStore.userInfo.username || '',
        content: topicText.value,
        time: currentTime,
        category: props.category,
        imageUrls: []
    };

    await sendTopic(cardData);
};

const sendTopic = async (cardData: SendTopic) => {
    try {
        const response = await axiosInstance.post('/addcard', cardData);
        toast.add({ severity: 'success', summary: '成功', detail: response.data.message || '发送成功！', life: 3000 });
        emit('topicSent');
        closeDialog();
    } catch (error: any) {
        handleSendError(error);
    }
};

const handleUploadError = (error: any) => {
    console.error("图片批量上传失败:", error);
    const uploadErrorMessage = error.response?.data?.message || `图片上传失败 (${selectedFiles.value.length}张)，话题未发送。`;
    toast.add({ severity: 'error', summary: '图片上传错误', detail: uploadErrorMessage, life: 4000 });
    isUploading.value = false;
    uploadProgress.value = 0;
};

const handleSendError = (error: any) => {
    console.error("发送失败:", error);
    const errorMessage = error.response?.data?.detail || error.response?.data?.message || '发送失败，请稍后重试';
    toast.add({ severity: 'error', summary: '错误', detail: errorMessage, life: 4000 });
    isUploading.value = false;
    uploadProgress.value = 0;
};

// 在组件卸载时清理
onUnmounted(() => {
    clearImages()
})

// 监听粘贴的图片，将其添加到 selectedFiles 和 imagePreviewUrls
watch(pastedImages, (newImages) => {
    if (newImages.length > 0) {
        newImages.forEach(async (imageUrl) => {
            // fetch Blob 对象
            const response = await fetch(imageUrl)
            const blob = await response.blob()
            // 生成文件名
            const fileName = `pasted-image-${Date.now()}-${Math.floor(Math.random()*10000)}.png`
            const file = new File([blob], fileName, { type: blob.type })
            // 限制最多3张
            if (selectedFiles.value.length < 3) {
                selectedFiles.value.push(file)
                imagePreviewUrls.value.push(imageUrl)
            } else {
                toast.add({ severity: 'warn', summary: '提示', detail: '最多只能选择3张图片。', life: 3000 });
            }
        })
        // 清空 pastedImages
        clearImages()
    }
})

// 新增 removeImage 方法，删除指定图片
const removeImage = (index: number) => {
    selectedFiles.value.splice(index, 1)
    imagePreviewUrls.value.splice(index, 1)
    if (fileInputRef.value) {
        fileInputRef.value.value = ''
    }
}

// 监听 paste 事件
useEventListener(document, 'paste', (e: ClipboardEvent) => {
    if (!e.clipboardData) return
    for (const item of e.clipboardData.items) {
        if (item.type.startsWith('image/')) {
            const file = item.getAsFile()
            if (file) {
                const url = URL.createObjectURL(file)
                pastedImages.value.push(url)
            }
        }
    }
})

// 处理粘贴事件
const handlePaste = (e: ClipboardEvent) => {
    if (!e.clipboardData) return
    for (const item of e.clipboardData.items) {
        if (item.type.startsWith('image/')) {
            const file = item.getAsFile()
            if (file) {
                if (selectedFiles.value.length < 3) {
                    const url = URL.createObjectURL(file)
                    selectedFiles.value.push(file)
                    imagePreviewUrls.value.push(url)
                } else {
                    toast.add({ severity: 'warn', summary: '提示', detail: '最多只能选择3张图片。', life: 3000 });
                }
            }
        }
    }
}
</script> 