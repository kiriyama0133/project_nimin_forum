<template>
<div>
    <div @click="router.push('/contentpage')" class="defaultcard bg-pink-50 rounded-lg shadow-lg transition-all 
        duration-500 transform hover:shadow-2xl hover:-translate-y-2 h-[10rem] line-clamp-5">
        <div class="p-4">
            <h2 class="text-lg  text-gray-800 mb-4">
                <slot name="title">
                    <div class="flex gap-4">
                        <p>No.{{ number }}</p>
                        <p>{{ id }}</p>
                    </div>
                </slot>
            </h2>
            <p class="text-gray-600">
               <slot name="content">
                <p>{{ content }}</p>
               </slot>
            </p>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
defineProps(['number','id','content'])
import { useRouter } from 'vue-router';
const router = useRouter()
</script>
<style scoped>
.defaultcard{
cursor: url('../assets/ani/link_2.png'), pointer;
}
</style>