<script setup lang="ts">
import { ref } from 'vue';
import FontSettings from '@/components/Preferences/FontSettings.vue';
import ThemeSettings from '@/components/Preferences/ThemeSettings.vue';
import NotificationSettings from '@/components/Preferences/NotificationSettings.vue';
import PrivacySettings from '@/components/Preferences/PrivacySettings.vue';

const activeTab = ref('font');
</script>

<template>
  <div class="preferences-container">
    <div class="tabs">
      <button 
        :class="['tab-button', { active: activeTab === 'font' }]"
        @click="activeTab = 'font'"
      >
        字体设置
      </button>
      <button 
        :class="['tab-button', { active: activeTab === 'theme' }]"
        @click="activeTab = 'theme'"
      >
        主题设置
      </button>
      <button 
        :class="['tab-button', { active: activeTab === 'notification' }]"
        @click="activeTab = 'notification'"
      >
        通知设置
      </button>
      <button 
        :class="['tab-button', { active: activeTab === 'privacy' }]"
        @click="activeTab = 'privacy'"
      >
        隐私设置
      </button>
    </div>

    <div class="content">
      <FontSettings v-if="activeTab === 'font'" />
      <ThemeSettings v-if="activeTab === 'theme'" />
      <NotificationSettings v-if="activeTab === 'notification'" />
      <PrivacySettings v-if="activeTab === 'privacy'" />
    </div>
  </div>
</template>

<style scoped>
.preferences-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  border-bottom: 1px solid #e5e7eb;
  padding-bottom: 1rem;
}

.tab-button {
  padding: 0.5rem 1rem;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 1rem;
  color: #6b7280;
  border-radius: 0.375rem;
  transition: all 0.2s;
}

.tab-button:hover {
  color: #2563eb;
  background-color: #f3f4f6;
}

.tab-button.active {
  color: #2563eb;
  font-weight: 600;
  background-color: #eff6ff;
}

.content {
  background-color: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

:root[class~="darkmode"] .content {
  background-color: #1f2937;
}

:root[class~="darkmode"] .tab-button {
  color: #9ca3af;
}

:root[class~="darkmode"] .tab-button:hover {
  color: #60a5fa;
  background-color: #374151;
}

:root[class~="darkmode"] .tab-button.active {
  color: #60a5fa;
  background-color: #1e3a8a;
}

:root[class~="darkmode"] .tabs {
  border-bottom-color: #374151;
}
</style> 