<template>
    <div class="loading-overlay" id="loading">
      <div class="spinner"></div>
      <p>加载中...</p>
    </div>
  </template>
  
  <script setup lang="ts">
import { onMounted } from 'vue';
onMounted(() => {
  const loading = document.getElementById('loading');
  if (loading) {
    // 延迟触发动画
    setTimeout(() => {
      loading.style.opacity = '1'; // 目标透明度
      loading.style.backgroundColor = 'rgba(255, 255, 255, 0.9)';
    }, 0); // 延迟 0 毫秒，确保初始样式生效
  }
});
  </script>
  
  <style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  opacity: 0; /* 初始透明度 */
  transition: transform 300ms ease, opacity 300ms ease; /* 动画过渡 */
}

.spinner {
width: 50px;
height: 50px;
border: 5px solid #ccc;
border-top-color: #818186;
border-radius: 50%;
animation: spin 1s linear infinite;
}

@keyframes spin {
to {
    transform: rotate(360deg);
}
}
</style>