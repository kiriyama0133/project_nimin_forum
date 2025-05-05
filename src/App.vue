<script setup lang="ts">

import { useRouter } from 'vue-router';
import Toast from 'primevue/toast';
// 控制骨架屏显示状态
const router = useRouter();

</script>

<template>
    <Toast/>
    <router-view>

    </router-view>
</template>

<style scoped>

</style>