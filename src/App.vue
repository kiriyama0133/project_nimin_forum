<script setup lang="ts">

import { useRouter } from 'vue-router';
// 控制骨架屏显示状态
const router = useRouter();
router.push('/loginview');
</script>

<template>
    <router-view>

    </router-view>
</template>

<style scoped>

</style>