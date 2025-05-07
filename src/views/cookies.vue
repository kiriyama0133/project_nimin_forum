<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Card from 'primevue/card';
import Button from 'primevue/button';
import Tag from 'primevue/tag';
import {useCounterStore} from '../stores/login_register';
import { useToast } from "primevue/usetoast";
import { addCookie, fetchUserCookies, getUserCookieNumber, setActiveBackendCookie, type CookieApiResponse } from '../utils/getCookies';
import type { Cookie, CookieResponse, UserCookieNumberResponse } from '../types/cookies';
const userStore = useCounterStore();
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

//获取用户获取cookie的剩余次数
const fetchUserCookieNumber = async () => {
  isLoading.value = true;
  try {
    const response: UserCookieNumberResponse = await getUserCookieNumber();
    remainingAttempts.value = response.number;
  } catch (error: any) {
    console.error('Failed to fetch user cookie number:', error);
    toast.add({ severity: 'error', summary: '错误', detail: error.message || '获取饼干剩余次数失败', life: 3000 });
  } finally {
    isLoading.value = false;
  }
}
const fetchUserCookieData = async () => {
  isLoading.value = true;
  try {
    const response: CookieResponse = await fetchUserCookies();
    
    userCookies.value = [];
    bannedCookies.value = [];

    const fetchedCookies: Cookie[] = response.data;
    console.log("Fetched cookies from backend:", fetchedCookies);

    fetchedCookies.forEach(backendCookie => {
      if (backendCookie.isbanned) {
        bannedCookies.value.push({
          id: backendCookie.name,
          name: backendCookie.name,
          status: 'banned',
        });
      } else {
        userCookies.value.push({
          id: backendCookie.name,
          name: backendCookie.name,
          status: backendCookie.inused ? 'in-use' : 'available',
        });
        userStore.userInfo.username = userCookies.value.find(c => c.status === 'in-use')?.name || '';
        console.log("检测到了现在正在使用",userStore.userInfo.username)
      }
    });
    
    console.log("Cookie data processed from backend.");

  } catch (error: any) {
    console.error('Failed to fetch user cookie data:', error);
    toast.add({ severity: 'error', summary: '错误', detail: error.message || '获取饼干列表失败', life: 3000 });
    userCookies.value = [];
    bannedCookies.value = [];
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchUserCookieData();
  fetchUserCookieNumber();
});

const requestNewCookie = async () => {
  isLoading.value = true;
  try {
    const apiResponse: CookieApiResponse = await addCookie();
    toast.add({
      severity: apiResponse.message.startsWith("Cookie '") ? 'success' : 'warn',
      summary: apiResponse.message.startsWith("Cookie '") ? '成功' : '提示',
      detail: apiResponse.message,
      life: 4000
    });

    if (apiResponse.message.startsWith("Cookie '")) {
      const match = apiResponse.message.match(/^Cookie '(.+?)' 添加成功，剩余cookies: (\d+)$/);
      if (match && match[1] && match[2]) {
        const newRemainingAttempts = parseInt(match[2], 10);
        remainingAttempts.value = newRemainingAttempts;
        await fetchUserCookieData();
      } else {
        console.warn("Could not parse cookie name or remaining attempts from success message:", apiResponse.message);
        await fetchUserCookieData(); 
      }
    } else if (apiResponse.message.includes("cookies不足")) {
      remainingAttempts.value = 0;
    } else {
    }

  } catch (error: any) {
    console.error('Request new cookie failed unexpectedly:', error);
    toast.add({ severity: 'error', summary: '错误', detail: '申请饼干失败，请稍后再试。', life: 3000 });
  } finally {
    isLoading.value = false;
  }
};

//启用饼干的部分
const setActiveCookie = async (selectedCookie: CookieInfo) => {
  isLoading.value = true;
  try {
    const response: CookieApiResponse = await setActiveBackendCookie(selectedCookie.id);

    if (response.message === "Cookie启用成功") {
      toast.add({ severity: 'success', summary: '成功', detail: `饼干 "${selectedCookie.name}" 已成功启用。`, life: 3000 });
      await fetchUserCookieData();
    } else {
      toast.add({ 
        severity: 'warn', 
        summary: '启用提示', 
        detail: response.message || '启用饼干时遇到问题。' , 
        life: 3000 
      });
      await fetchUserCookieData();
    }
  } catch (error: any) {
    console.error('Failed to set active cookie:', error);
    toast.add({ severity: 'error', summary: '错误', detail: error.message || '启用饼干失败，请稍后再试。', life: 3000 });
    await fetchUserCookieData();
  } finally {
    isLoading.value = false;
  }
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
