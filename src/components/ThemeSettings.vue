<script setup lang="ts">
import { ref } from 'vue';
import { useDarkmode } from '../stores/darkmode';

const darkstore = useDarkmode();
const followSystem = ref(false);

const toggleDarkMode = () => {
  document.documentElement.classList.toggle('darkmode');
  darkstore.Darkmode = !darkstore.Darkmode;
};

const toggleFollowSystem = () => {
  followSystem.value = !followSystem.value;
  // 实现跟随系统的逻辑
  if (followSystem.value) {
    // 检查系统主题
    const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    if (darkModeMediaQuery.matches) {
      document.documentElement.classList.add('darkmode');
      darkstore.Darkmode = true;
    } else {
      document.documentElement.classList.remove('darkmode');
      darkstore.Darkmode = false;
    }
  }
};
</script>

<template>
  <div class="theme-settings">
    <h2 class="section-title">主题设置</h2>
    
    <div class="setting-item">
      <span>深色模式</span>
      <label class="toggle">
        <input type="checkbox" :checked="darkstore.Darkmode" @change="toggleDarkMode" />
        <span class="toggle-slider"></span>
      </label>
    </div>
    
    <div class="setting-item">
      <span>跟随系统</span>
      <label class="toggle">
        <input type="checkbox" v-model="followSystem" @change="toggleFollowSystem" />
        <span class="toggle-slider"></span>
      </label>
    </div>
  </div>
</template>

<style scoped>
.theme-settings {
  padding: 1rem;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.setting-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.toggle {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
}

.toggle input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #e5e7eb;
  transition: .4s;
  border-radius: 24px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: #2563eb;
}

input:checked + .toggle-slider:before {
  transform: translateX(20px);
}

:root[class~="darkmode"] .toggle-slider {
  background-color: #4b5563;
}
</style> 