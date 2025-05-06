<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Card from 'primevue/card';
import Button from 'primevue/button';
import Tag from 'primevue/tag';
import { useToast } from "primevue/usetoast";
import { addCookie, type CookieApiResponse } from '../utils/getCookies';

const toast = useToast();

interface CookieInfo {
  id: string;
  name: string;
  status: 'available' | 'in-use' | 'banned';
  reason?: string;
}

const userCookies = ref<CookieInfo[]>([]);
const bannedCookies = ref<CookieInfo[]>([]);
const remainingAttempts = ref<number>(0);
const isLoading = ref(false);

const fetchUserCookieData = async () => {
  isLoading.value = true;
  console.log("Fetching initial cookie data...");
  await new Promise(resolve => setTimeout(resolve, 1000));

  userCookies.value = [
    { id: 'mock-id-1', name: '初始饼干A', status: 'available' },
    { id: 'mock-id-2', name: '初始饼干B (在用)', status: 'in-use' },
  ];
  bannedCookies.value = [
    { id: 'mock-ban-1', name: '违规饼干X', status: 'banned', reason: '示例原因' }
  ];
  remainingAttempts.value = 3;

  console.log("Initial cookie data fetched (mocked).");
  isLoading.value = false;
};

onMounted(() => {
  fetchUserCookieData();
});

const requestNewCookie = async () => {
  isLoading.value = true;
  try {
    const response: CookieApiResponse = await addCookie();
    toast.add({
      severity: response.message.startsWith("Cookie '") ? 'success' : 'warn',
      summary: response.message.startsWith("Cookie '") ? '成功' : '提示',
      detail: response.message,
      life: 4000
    });

    if (response.message.startsWith("Cookie '")) {
      const match = response.message.match(/^Cookie '(.+?)' 添加成功，剩余cookies: (\d+)$/);
      if (match && match[1] && match[2]) {
        const newCookieNameFromAPI = match[1];
        const newRemainingAttempts = parseInt(match[2], 10);

        userCookies.value.push({
          id: `new-${newCookieNameFromAPI}-${Date.now()}`,
          name: newCookieNameFromAPI,
          status: 'available'
        });
        remainingAttempts.value = newRemainingAttempts;
      } else {
        console.warn("Could not parse cookie name or remaining attempts from success message:", response.message);
        await fetchUserCookieData();
      }
    } else if (response.message.includes("cookies不足")) {
      remainingAttempts.value = 0;
    } else {
    }

  } catch (error) {
    console.error('Request new cookie failed unexpectedly:', error);
    toast.add({ severity: 'error', summary: '错误', detail: '申请饼干失败，请稍后再试。', life: 3000 });
  } finally {
    isLoading.value = false;
  }
};

const setActiveCookie = async (selectedCookie: CookieInfo) => {
  isLoading.value = true;
  console.log(`Attempting to set cookie "${selectedCookie.name}" as active.`);
  await new Promise(resolve => setTimeout(resolve, 500));

  let previouslyActiveName: string | null = null;
  userCookies.value.forEach(cookie => {
    if (cookie.id === selectedCookie.id) {
      cookie.status = 'in-use';
    } else if (cookie.status === 'in-use') {
      previouslyActiveName = cookie.name;
      cookie.status = 'available';
    }
  });
  toast.add({ severity: 'info', summary: '切换成功', detail: `"${selectedCookie.name}" 已设为当前使用。`, life: 3000 });
  console.log(`Set cookie "${selectedCookie.name}" as active. Deactivated: "${previouslyActiveName || 'None'}"`);
  isLoading.value = false;
};

</script>

<template>
  <div class="p-4 md:p-6 lg:p-8 bg-gray-100 min-h-screen">
    <div class="max-w-screen-xl mx-auto">
      <h1 class="text-3xl font-bold mb-8 text-center text-gray-700">饼干管理中心</h1>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <Card class="shadow-lg hover:shadow-xl transition-shadow duration-300">
          <template #title><span class="text-xl font-semibold text-blue-700">申请与状态</span></template>
          <template #content>
            <p class="mb-3 text-gray-600">剩余申请次数: <Tag :value="remainingAttempts.toString()" severity="warning" class="text-lg font-bold"></Tag> 次</p>
            <Button label="申请新饼干" icon="pi pi-plus-circle" @click="requestNewCookie" :disabled="remainingAttempts <= 0" />
          </template>
        </Card>
        
        <Card class="shadow-lg hover:shadow-xl transition-shadow duration-300">
          <template #title><span class="text-xl font-semibold text-purple-700">账号信息 (示例)</span></template>
          <template #content>
            <div v-if="userCookies.find(c => c.status === 'in-use')">
              <p class="text-gray-700">当前使用饼干: 
                <span class="font-semibold text-green-600">{{ userCookies.find(c => c.status === 'in-use')?.name }}</span>
              </p>
            </div>
            <p v-else class="text-gray-500 italic">当前没有选择使用的饼干。</p>
          </template>
        </Card>
      </div>

      <Card class="shadow-lg hover:shadow-xl transition-shadow duration-300 mb-6">
        <template #title><span class="text-xl font-semibold text-green-700">我的饼干 (选择使用)</span></template>
        <template #content>
          <ul v-if="userCookies.length > 0" class="space-y-3">
            <li v-for="cookie in userCookies" :key="cookie.id" class="p-3 bg-gray-50 rounded-lg flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 shadow-sm">
              <span class="font-medium text-gray-800">{{ cookie.name }}</span>
              <div>
                <Tag v-if="cookie.status === 'in-use'" value="正在使用" severity="success"></Tag>
                <Button v-else-if="cookie.status === 'available'" label="使用此饼干" icon="pi pi-check-circle" @click="setActiveCookie(cookie)" class="p-button-sm p-button-outlined" />
              </div>
            </li>
          </ul>
          <p v-else class="text-gray-500 italic">您还没有可用的饼干，请先申请。</p>
        </template>
      </Card>

      <Card class="shadow-lg hover:shadow-xl transition-shadow duration-300 border-t-4 border-red-500">
        <template #title><span class="text-xl font-semibold text-red-700">违禁 / 封禁的饼干</span></template>
        <template #content>
          <ul v-if="bannedCookies.length > 0" class="space-y-2">
            <li v-for="cookie in bannedCookies" :key="cookie.id" class="p-2 bg-red-50 rounded-md">
              <div class="flex justify-between items-center">
                <span class="font-medium">{{ cookie.name }}</span>
                <Tag :value="'已封禁'" severity="danger"></Tag>
              </div>
              <p v-if="cookie.reason" class="text-sm text-red-600 italic mt-1">原因: {{ cookie.reason }}</p>
            </li>
          </ul>
          <p v-else class="text-gray-500 italic">没有被封禁的饼干记录。</p>
        </template>
      </Card>
    </div>
  </div>
</template>

<style scoped>
.p-card .p-card-title {
  font-size: 1.25rem;
}
</style>
