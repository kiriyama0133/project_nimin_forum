<template>
    <div class=" rounded-lg" style="box-shadow: 0 0 10px 5px rgba(255, 255, 255, 0.5);">
        <div class="defaultcard rounded-lg shadow-lg transition-all 
            duration-200 transform hover:shadow-2xl hover:-translate-y-2">
            <div class="p-4">
                <h2 class="text-lg   mb-3">
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
                <h3 v-if="props.reply" class="text-lg   mb-4 bg-pink-100">
                    <slot name="reply">
                        <div class="flex gap-4">
                            <p>>>></p>
                            <p class=" text-black">{{ props.reply }}</p>
                        </div>
                    </slot>
                </h3>
                <p class="">
                   <slot name="content">
                    <p>{{ props.content }}</p>
                   </slot>
                </p>
                <div class=" flex justify-end items-center gap-2">
                    <slot name="end">
                        <div class="card flex">
                            <ToggleButton v-model="checked" off-icon="pi pi-thumbs-up" on-icon="pi pi-thumbs-up-fill" 
                             class="w-20" aria-label="Do you confirm"
                              :off-label="props.thumbs !== undefined ? Number(props.thumbs).toString() : '0'"
                              :on-label="props.thumbs !== undefined ? (Number(props.thumbs) + 1).toString() : '1'"
                              />
                        </div> 
                        <Button :alt="props.index" @click=refresh variant="outlined" 
                        raised style="font-size: 10px;"
                        class="text w-18 h-8" label="回复" icon="pi pi-reply" />
                    </slot>
                </div>
            </div>
            </div>
        </div>
    </template>
<script lang="ts" setup>
import Button from 'primevue/button';
import 'primeicons/primeicons.css';
import {useDialogStore} from '../stores/dialog'
import ToggleButton from 'primevue/togglebutton';
import { ref, defineProps } from 'vue';

//这里要写一个👍的更新
const dialog = useDialogStore();
const checked = ref(false);
function refresh(){
    dialog.Dialogvisible = true;
    dialog.replyuser = props.id
}

// Define props with types for better clarity and type safety
const props = defineProps<{
  id: string;
  reply?: string;
  content: string;
  index: number | string;
  thumbs?: number | string; // Allow string to handle cases where it might be passed as such, Number() will parse
  time: string;
  number: number | string;
}>();

</script>
<style scoped>
.defaultcard{
cursor: url('../assets/ani/select_2.png'), pointer;
}
</style>