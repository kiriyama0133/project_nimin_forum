<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { ElMessage } from 'element-plus';

//------->主字体设置
const fontFamilies = [
  { label: '微软雅黑', value: 'microsoft-yahei', class: 'font-microsoft-yahei' },
  { label: '宋体', value: 'simsun', class: 'font-simsun' },
  { label: '黑体', value: 'simhei', class: 'font-simhei' },
  { label: '楷体', value: 'kaiti', class: 'font-kaiti' },
  { label: 'Arial', value: 'arial', class: 'font-arial' }
];
const fontSizes = [
  { label: '小', value: 'small', class: 'text-small' },
  { label: '中', value: 'medium', class: 'text-medium' },
  { label: '大', value: 'large', class: 'text-large' }
];
//-------<主字体设置

//------->回复的字体设置
const replyTextStyles = [
  { label: '默认', value: 'default', class: 'reply-default' },
  { label: '粉色', value: 'pink', class: 'reply-pink' },
  { label: '蓝色', value: 'blue', class: 'reply-blue' },
  { label: '绿色', value: 'green', class: 'reply-green' }
];
const replyTextSize = [
  { label: '小', value: 'small', class: 'reply-text-small' },
  { label: '中', value: 'medium', class: 'reply-text-medium' },
  { label: '大', value: 'large', class: 'reply-text-large' }
];
//------->回复的字体设置

//------->用户ID和Mate的字体设置
const userIdStyles = [
  { label: '默认', value: 'default', class: 'user-id-default' },
  { label: '粉色', value: 'pink', class: 'user-id-pink' },
  { label: '蓝色', value: 'blue', class: 'user-id-blue' },
  { label: '绿色', value: 'green', class: 'user-id-green' }
];

const userIdSizes = [
  { label: '小', value: 'small', class: 'user-id-small' },
  { label: '中', value: 'medium', class: 'user-id-medium' },
  { label: '大', value: 'large', class: 'user-id-large' }
];

const mateStyles = [
  { label: '默认', value: 'default', class: 'mate-default' },
  { label: '粉色', value: 'pink', class: 'mate-pink' },
  { label: '蓝色', value: 'blue', class: 'mate-blue' },
  { label: '绿色', value: 'green', class: 'mate-green' }
];

const mateSizes = [
  { label: '小', value: 'small', class: 'mate-small' },
  { label: '中', value: 'medium', class: 'mate-medium' },
  { label: '大', value: 'large', class: 'mate-large' }
];
//------->用户ID和Mate的字体设置

//------->默认字体设置
const selectedFont = ref(fontFamilies[0].value); // 默认字体为微软雅黑
const selectedReplyStyle = ref(replyTextStyles[2].value); // 默认字体为蓝色
const selectedReplySize = ref(replyTextSize[1].value);
const selectedUserIdStyle = ref(userIdStyles[3].value); // 默认字体为绿色
const selectedUserIdSize = ref(userIdSizes[1].value);
const selectedMateStyle = ref(mateStyles[3].value); // 默认字体为绿色
const selectedMateSize = ref(mateSizes[0].value);
//------->默认字体设置

const applyFontSettings = () => {
  // 移除所有字体类
  document.body.classList.remove(...fontFamilies.map(f => f.class));
  // 移除所有字体大小类
  document.body.classList.remove(...fontSizes.map(s => s.class));
  // 移除所有回复文本样式类
  document.body.classList.remove(...replyTextStyles.map(s => s.class));
  // 移除所有回复文本大小类
  document.body.classList.remove(...replyTextSize.map(s => s.class));
  // 移除所有用户ID样式类
  document.body.classList.remove(...userIdStyles.map(s => s.class));
  // 移除所有用户ID大小类
  document.body.classList.remove(...userIdSizes.map(s => s.class));
  // 移除所有Mate样式类
  document.body.classList.remove(...mateStyles.map(s => s.class));
  // 移除所有Mate大小类
  document.body.classList.remove(...mateSizes.map(s => s.class));
  
  // 添加选中的字体类
  const selectedFontClass = fontFamilies.find(f => f.value === selectedFont.value)?.class;
  if (selectedFontClass) {
    document.body.classList.add(selectedFontClass);
  }

  // 添加选中的回复文本样式类
  const selectedReplyClass = replyTextStyles.find(s => s.value === selectedReplyStyle.value)?.class;
  if (selectedReplyClass) {
    document.body.classList.add(selectedReplyClass);
  }

  // 添加选中的回复文本大小类
  const selectedReplySizeClass = replyTextSize.find(s => s.value === selectedReplySize.value)?.class;
  if (selectedReplySizeClass) {
    document.body.classList.add(selectedReplySizeClass);
  }

  // 添加选中的用户ID样式类
  const selectedUserIdStyleClass = userIdStyles.find(s => s.value === selectedUserIdStyle.value)?.class;
  if (selectedUserIdStyleClass) {
    document.body.classList.add(selectedUserIdStyleClass);
  }

  // 添加选中的用户ID大小类
  const selectedUserIdSizeClass = userIdSizes.find(s => s.value === selectedUserIdSize.value)?.class;
  if (selectedUserIdSizeClass) {
    document.body.classList.add(selectedUserIdSizeClass);
  }

  // 添加选中的Mate样式类
  const selectedMateStyleClass = mateStyles.find(s => s.value === selectedMateStyle.value)?.class;
  if (selectedMateStyleClass) {
    document.body.classList.add(selectedMateStyleClass);
  }

  // 添加选中的Mate大小类
  const selectedMateSizeClass = mateSizes.find(s => s.value === selectedMateSize.value)?.class;
  if (selectedMateSizeClass) {
    document.body.classList.add(selectedMateSizeClass);
  }
  
  // 保存设置到本地存储
  localStorage.setItem('fontFamily', selectedFont.value);
  localStorage.setItem('replyStyle', selectedReplyStyle.value);
  localStorage.setItem('replySize', selectedReplySize.value);
  localStorage.setItem('userIdStyle', selectedUserIdStyle.value);
  localStorage.setItem('userIdSize', selectedUserIdSize.value);
  localStorage.setItem('mateStyle', selectedMateStyle.value);
  localStorage.setItem('mateSize', selectedMateSize.value);
  
  ElMessage({
    message: '字体设置已保存',
    type: 'success',
    duration: 2000
  });
};

onMounted(() => {
  // 从本地存储加载设置
  const savedFont = localStorage.getItem('fontFamily');
  const savedReplyStyle = localStorage.getItem('replyStyle');
  const savedReplySize = localStorage.getItem('replySize');
  const savedUserIdStyle = localStorage.getItem('userIdStyle');
  const savedUserIdSize = localStorage.getItem('userIdSize');
  const savedMateStyle = localStorage.getItem('mateStyle');
  const savedMateSize = localStorage.getItem('mateSize');
  
  if (savedFont) selectedFont.value = savedFont;
  if (savedReplyStyle) selectedReplyStyle.value = savedReplyStyle;
  if (savedReplySize) selectedReplySize.value = savedReplySize;
  if (savedUserIdStyle) selectedUserIdStyle.value = savedUserIdStyle;
  if (savedUserIdSize) selectedUserIdSize.value = savedUserIdSize;
  if (savedMateStyle) selectedMateStyle.value = savedMateStyle;
  if (savedMateSize) selectedMateSize.value = savedMateSize;

});
</script>

<template>
  <div class="font-settings p-4">
    <h2 class="text-xl mb-4">字体设置</h2>
    
    <div class="mb-4">
      <label class="block mb-2">字体选择</label>
      <select v-model="selectedFont" class="w-full p-2 border rounded">
        <option v-for="font in fontFamilies" :key="font.value" :value="font.value">
          {{ font.label }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <label class="block mb-2">回复文本样式</label>
      <select v-model="selectedReplyStyle" class="w-full p-2 border rounded">
        <option v-for="style in replyTextStyles" :key="style.value" :value="style.value">
          {{ style.label }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <select v-model="selectedReplySize" class="w-full p-2 border rounded">
        <option v-for="size in replyTextSize" :key="size.value" :value="size.value">
          {{ size.label }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <label class="block mb-2">用户ID样式</label>
      <select v-model="selectedUserIdStyle" class="w-full p-2 border rounded">
        <option v-for="style in userIdStyles" :key="style.value" :value="style.value">
          {{ style.label }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <select v-model="selectedUserIdSize" class="w-full p-2 border rounded">
        <option v-for="size in userIdSizes" :key="size.value" :value="size.value">
          {{ size.label }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <label class="block mb-2">Mate样式</label>
      <select v-model="selectedMateStyle" class="w-full p-2 border rounded">
        <option v-for="style in mateStyles" :key="style.value" :value="style.value">
          {{ style.label }}
        </option>
      </select>
    </div>

    <div class="mb-4">
      <select v-model="selectedMateSize" class="w-full p-2 border rounded">
        <option v-for="size in mateSizes" :key="size.value" :value="size.value">
          {{ size.label }}
        </option>
      </select>
    </div>
    
    <button @click="applyFontSettings" 
            class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
      应用设置
    </button>
  </div>
</template>

<style scoped>
.font-settings {
  max-width: 400px;
  margin: 0 auto;
}

/* 字体类 */
.font-microsoft-yahei {
  font-family: 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}

.font-simsun {
  font-family: 'SimSun', '宋体', serif;
}

.font-simhei {
  font-family: 'SimHei', '黑体', sans-serif;
}

.font-kaiti {
  font-family: 'KaiTi', '楷体', serif;
}

.font-arial {
  font-family: Arial, sans-serif;
}

/* 字体大小类 */
.text-small {
  font-size: 14px;
}

.text-medium {
  font-size: 16px;
}

.text-large {
  font-size: 18px;
}

/* 回复文本样式类 */
:global(.reply-default .Reply_text) {
  color: #666;
  font-weight: normal;
}

:global(.reply-pink .Reply_text) {
  color: #ff69b4;
  font-weight: bold;
}

:global(.reply-blue .Reply_text) {
  color: #1e90ff;
  font-weight: bold;
}

:global(.reply-green .Reply_text) {
  color: #32cd32;
  font-weight: bold;
}

/* 回复文本大小类 */
:global(.reply-text-small .Reply_text) {
  font-size: 12px;
}

:global(.reply-text-medium .Reply_text) {
  font-size: 14px;
}

:global(.reply-text-large .Reply_text) {
  font-size: 16px;
}

/* 用户ID样式类 */
:global(.user-id-default .User_Id) {
  color: #666;
  font-weight: normal;
}

:global(.user-id-pink .User_Id) {
  color: #ff69b4;
  font-weight: bold;
}

:global(.user-id-blue .User_Id) {
  color: #1e90ff;
  font-weight: bold;
}

:global(.user-id-green .User_Id) {
  color: #32cd32;
  font-weight: bold;
}

/* 用户ID大小类 */
:global(.user-id-small .User_Id) {
  font-size: 12px;
}

:global(.user-id-medium .User_Id) {
  font-size: 14px;
}

:global(.user-id-large .User_Id) {
  font-size: 16px;
}

/* Mate样式类 */
:global(.mate-default .Mate) {
  color: #666;
  font-weight: normal;
}

:global(.mate-pink .Mate) {
  color: #ff69b4;
  font-weight: bold;
}

:global(.mate-blue .Mate) {
  color: #1e90ff;
  font-weight: bold;
}

:global(.mate-green .Mate) {
  color: #32cd32;
  font-weight: bold;
}

/* Mate大小类 */
:global(.mate-small .Mate) {
  font-size: 12px;
}

:global(.mate-medium .Mate) {
  font-size: 14px;
}

:global(.mate-large .Mate) {
  font-size: 16px;
}
</style> 