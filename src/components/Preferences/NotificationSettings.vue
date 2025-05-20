<script setup lang="ts">
import { ref } from 'vue';

const settings = ref({
  newMessage: true,
  systemNotification: true
});

const saveSettings = () => {
  localStorage.setItem('notificationSettings', JSON.stringify(settings.value));
};
</script>

<template>
  <div class="notification-settings">
    <h2 class="section-title">通知设置</h2>
    
    <div class="setting-item">
      <span>新消息通知</span>
      <label class="toggle">
        <input type="checkbox" v-model="settings.newMessage" @change="saveSettings" />
        <span class="toggle-slider"></span>
      </label>
    </div>
    
    <div class="setting-item">
      <span>系统通知</span>
      <label class="toggle">
        <input type="checkbox" v-model="settings.systemNotification" @change="saveSettings" />
        <span class="toggle-slider"></span>
      </label>
    </div>
  </div>
</template>

<style scoped>
.notification-settings {
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