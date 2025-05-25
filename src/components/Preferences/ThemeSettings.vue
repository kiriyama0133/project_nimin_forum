<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { useDarkmode } from '../../stores/darkmode';
import Button from 'primevue/button';
import Slider from 'primevue/slider';

const darkstore = useDarkmode();
const followSystem = ref(false);
const backgroundImage = ref('');
const backgroundOpacity = ref(0.5);
const sliderValue = ref(50);
const enableBlur = ref(false);

// 从localStorage加载设置
const loadSettings = () => {
  const savedSettings = localStorage.getItem('themeSettings');
  if (savedSettings) {
    const settings = JSON.parse(savedSettings);
    backgroundImage.value = settings.backgroundImage || '';
    sliderValue.value = settings.sliderValue || 50;
    enableBlur.value = settings.enableBlur || false;
    
    // 应用保存的设置
    if (backgroundImage.value) {
      document.documentElement.style.setProperty('--background-image', backgroundImage.value);
    }
    document.documentElement.style.setProperty('--background-opacity', (1 - sliderValue.value / 100).toString());
    document.documentElement.style.setProperty('--enable-blur', enableBlur.value ? 'blur(10px)' : 'none');
  }
};

// 保存设置到localStorage
const saveSettings = () => {
  const settings = {
    backgroundImage: backgroundImage.value,
    sliderValue: sliderValue.value,
    enableBlur: enableBlur.value
  };
  localStorage.setItem('themeSettings', JSON.stringify(settings));
};

// 监听滑块值变化
watch(sliderValue, (newValue) => {
  backgroundOpacity.value = newValue / 100;
  document.documentElement.style.setProperty('--background-opacity', (1 - newValue / 100).toString());
  saveSettings();
});

// 监听背景图片变化
watch(backgroundImage, (newValue) => {
  if (newValue) {
    const imageUrl = newValue.startsWith('data:') ? newValue : `url(${newValue})`;
    document.documentElement.style.setProperty('--background-image', imageUrl);
  } else {
    document.documentElement.style.setProperty('--background-image', 'none');
  }
  saveSettings();
});

// 监听毛玻璃效果变化
watch(enableBlur, (newValue) => {
  document.documentElement.style.setProperty('--enable-blur', newValue ? 'blur(10px)' : 'none');
  saveSettings();
});

// 在组件挂载时加载设置
onMounted(() => {
  loadSettings();
});

// 黑夜模式

const toggleDarkMode = () => {
  document.querySelectorAll('.main-page').forEach(el => {
    if (el.classList.contains('bg-gray-100')) {
      el.classList.remove('bg-gray-100');
      el.classList.add('bg-gray-900');
    } else if (el.classList.contains('bg-gray-900')) {
      el.classList.remove('bg-gray-900');
      el.classList.add('bg-gray-100');
    }
  });

  document.documentElement.classList.toggle('darkmode');
  darkstore.Darkmode = !darkstore.Darkmode;
};
const toggleFollowSystem = () => {
  followSystem.value = !followSystem.value;
  if (followSystem.value) {
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

// 处理背景图片上传
const handleBackgroundImageUpload = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      if (e.target?.result) {
        backgroundImage.value = e.target.result as string;
        console.log('Background image loaded:', backgroundImage.value); // 调试日志
      }
    };
    reader.readAsDataURL(file);
  }
};

// 清除背景图片
const clearBackgroundImage = () => {
  backgroundImage.value = '';
  document.documentElement.style.setProperty('--background-image', 'none');
  const input = document.querySelector('input[type="file"]') as HTMLInputElement;
  if (input) {
    input.value = '';
  }
  saveSettings();
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

    <div class="setting-item background-image-setting">
      <span>背景图片</span>
      <div class="background-controls">
        <input 
          type="file" 
          accept="image/*" 
          @change="handleBackgroundImageUpload"
          class="file-input"
          id="background-image-input"
        />
        <label for="background-image-input" class="upload-btn">
          <i class="pi" :class="backgroundImage ? 'pi-image' : 'pi-upload'"></i>
          <span class="upload-text">{{ backgroundImage ? '更换图片' : '选择图片' }}</span>
        </label>
        <Button 
          v-if="backgroundImage" 
          @click="clearBackgroundImage"
          icon="pi pi-times"
          severity="danger"
          text
          rounded
          aria-label="清除背景图片"
        />
      </div>
    </div>

    <div class="setting-item opacity-setting">
      <span>背景透明度</span>
      <div class="opacity-control">
        <Slider 
          v-model="sliderValue"
          :min="0" 
          :max="100" 
          :step="1"
          class="opacity-slider"
        />
        <span class="opacity-value">{{ sliderValue }}%</span>
      </div>
    </div>

    <div class="setting-item">
      <span>毛玻璃效果</span>
      <label class="toggle">
        <input type="checkbox" v-model="enableBlur" />
        <span class="toggle-slider"></span>
      </label>
    </div>
  </div>
</template>

<style scoped>
.theme-settings {
  padding: 1rem;
  max-width: 100%;
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
  flex-wrap: wrap;
  gap: 0.5rem;
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

.background-controls {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.file-input {
  display: none;
}

.upload-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  font-size: 0.875rem;
  transition: background-color 0.2s;
}

.upload-btn:hover {
  background-color: #1d4ed8;
}

.upload-text {
  display: none;
}

@media (min-width: 640px) {
  .upload-text {
    display: inline;
  }
}

.opacity-setting {
  flex-direction: column;
  align-items: stretch;
}

.opacity-control {
  display: flex;
  align-items: center;
  gap: 1rem;
  width: 100%;
  margin-top: 0.5rem;
}

.opacity-slider {
  flex: 1;
  min-width: 150px;
}

:deep(.p-slider) {
  width: 100%;
}

:deep(.p-slider .p-slider-handle) {
  width: 1.5rem;
  height: 1.5rem;
  margin-top: -0.75rem;
}

:deep(.p-slider .p-slider-range) {
  background: #2563eb;
}

:deep(.p-slider:not(.p-disabled) .p-slider-handle:hover) {
  background: #1d4ed8;
  border-color: #1d4ed8;
}

.opacity-value {
  min-width: 3rem;
  text-align: right;
}

@media (min-width: 640px) {
  .opacity-setting {
    flex-direction: row;
    align-items: center;
  }

  .opacity-control {
    margin-top: 0;
    width: auto;
  }
}

.darkmode{
    background-color: #18181a;
}
</style> 