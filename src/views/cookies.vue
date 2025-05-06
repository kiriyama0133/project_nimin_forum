<script setup lang="ts">
import { ref } from 'vue';
import Card from 'primevue/card';
import Button from 'primevue/button';
import Tag from 'primevue/tag';
import { useToast } from "primevue/usetoast"; // Import if needed for user feedback

const toast = useToast(); // Initialize if using

interface CookieInfo {
  id: string;
  name: string;
  status: 'available' | 'in-use' | 'banned'; // Status types
  reason?: string; // For banned cookies
}

// Combined list for user's non-banned cookies
const userCookies = ref<CookieInfo[]>([
  { id: 'req1', name: '饼干A', status: 'available' },
  { id: 'req2', name: '饼干B', status: 'available' },
  { id: 'use1', name: '饼干C (之前默认使用)', status: 'in-use' },
]);

const bannedCookies = ref<CookieInfo[]>([
  { id: 'ban1', name: '饼干D (违规)', status: 'banned', reason: '滥用权限' },
  { id: 'ban2', name: '饼干E (过期)', status: 'banned', reason: '已过期自动封禁' },
]);

const remainingAttempts = ref<number>(3);

const requestNewCookie = () => {
  if (remainingAttempts.value > 0) {
    remainingAttempts.value--;
    const newCookieId = `cookie-${Date.now().toString().slice(-6)}`;
    userCookies.value.push({
      id: newCookieId,
      name: `新饼干 ${newCookieId.slice(-4)}`,
      status: 'available'
    });
    toast.add({ severity: 'success', summary: '成功', detail: '新饼干已申请！', life: 3000 });
  } else {
    console.log('No remaining attempts to request a new cookie.');
    toast.add({ severity: 'warn', summary: '提示', detail: '没有剩余申请次数了。', life: 3000 });
  }
};

const setActiveCookie = (selectedCookie: CookieInfo) => {
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
  // Here you would typically also notify your backend/update global state
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
            <!-- You can add other account related info here -->
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
