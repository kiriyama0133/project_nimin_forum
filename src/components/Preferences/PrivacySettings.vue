<script setup lang="ts">
import { ref } from 'vue';

const settings = ref({
  dataCollection: false,
  onlineStatus: true
});

const saveSettings = () => {
  localStorage.setItem('privacySettings', JSON.stringify(settings.value));
};
</script>

<template>
  <div class="privacy-settings">
    <h2 class="section-title">隐私设置</h2>
    
    <div class="setting-item">
      <span>允许收集使用数据</span>
      <label class="toggle">
        <input type="checkbox" v-model="settings.dataCollection" @change="saveSettings" />
        <span class="toggle-slider"></span>
      </label>
    </div>
    
    <div class="setting-item">
      <span>显示在线状态</span>
      <label class="toggle">
        <input type="checkbox" v-model="settings.onlineStatus" @change="saveSettings" />
        <span class="toggle-slider"></span>
      </label>
    </div>
  </div>
</template>

<style scoped>
.privacy-settings {
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