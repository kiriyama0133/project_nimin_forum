<script setup lang="ts">
import bg from '@/assets/bg/defalut.jpg'
</script>
<template>
    <div alt="亚文化的首页的头顶区域" class="flex p-4 justify-center gap-10">
        <slot name="header">
            <img :src="bg" class="w-30 h-30 object-cover"/>
            <span>
                这里是亚文化头部的插槽，默认则使用这个占位
            </span>
            <span>
                内容请看下方的插槽
            </span>
        </slot>
    </div>
</template>