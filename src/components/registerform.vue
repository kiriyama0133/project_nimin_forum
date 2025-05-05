<script lang="ts" setup>
import { ElMessage } from 'element-plus';
import { useCounterStore } from '../stores/login_register';
import { UsersService, OpenAPI } from '../client';
import { ref } from 'vue';
import type { UserRegister } from '../client';

const store = useCounterStore();
OpenAPI.BASE = 'https://localhost:8000';

function goToLogin() {
  store.homepage = 'login';
}

let RegisterData = ref<UserRegister>({
  email: '',
  password: '',
  full_name: ''
});

const RegisterSend = async () => {
  if (!RegisterData.value.email || !RegisterData.value.password) {
      ElMessage({
          message: '请输入邮箱和密码',
          type: 'warning',
          duration: 3000
      });
      return;
  }
   if (RegisterData.value.password.length < 8) {
       ElMessage({
          message: '密码长度不能少于8位',
          type: 'warning',
          duration: 3000
      });
      return;
   }

  store.loading = true;
  try {
    const response = await UsersService.registerUser({
      requestBody: RegisterData.value
    });

    console.log('Registration Successful:', response);

    ElMessage({
      message: '注册成功！请登录。',
      type: 'success',
      duration: 2000
    });

    store.homepage = 'login';

  } catch (error: any) {
    console.error('注册请求失败:', error);
    let errorMessage = '注册失败，请稍后重试。';
    if (error?.status === 400) { 
        if (error.body?.detail?.includes('already exists')) {
             errorMessage = '注册失败：该邮箱已被注册。';
        } else {
             errorMessage = '注册失败：输入信息有误或邮箱已被使用。';
        }
    } else if (error?.body?.detail) {
        errorMessage = `注册失败：${error.body.detail[0]?.msg || '输入验证失败'}`;
    }
    ElMessage({
        message: errorMessage,
        type: 'error',
        duration: 4000
      });
  } finally {
    store.loading = false;
  }
};

function handleRegister() {
  RegisterSend();
}
</script>

<template>
  <div class="">
    <!-- Email Input -->
    <div class="flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 mb-5">
      <el-icon class="text-gray-500 mr-2"><Message /></el-icon>
      <input
        v-model="RegisterData.email"
        type="email"
        placeholder="请输入邮箱"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
    </div>

    <!-- Password Input -->
    <div class="flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 mb-5">
      <el-icon class="text-gray-500 mr-2"><Lock /></el-icon>
      <input
        v-model="RegisterData.password"
        type="password"
        placeholder="请输入密码 (至少8位)"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
    </div>

    <!-- Full Name Input (Optional) -->
    <div class="flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 mb-5">
       <el-icon class="text-gray-500 mr-2"><User /></el-icon>
      <input
        v-model="RegisterData.full_name"
        type="text"
        placeholder="请输入姓名 (可选)"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
    </div>

    <!-- Buttons -->
    <div class="flex justify-between items-center m-5">
      <!-- Register Button -->
      <button
        @click="handleRegister"
        class="btn w-15 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
        :disabled="store.loading"
      >
        注册
      </button>

      <!-- Back to Login Button -->
      <button
        @click="goToLogin"
        class="btn w-18 py-2 bg-gray-100 text-gray-700 font-semibold rounded-lg shadow-md hover:bg-gray-200 hover:shadow-lg transition duration-300"
        :disabled="store.loading"
      >
        返回登录
      </button>
    </div>
  </div>
</template>

<style scoped>
.text {
  cursor: url('../assets/ani/text_2.png'), pointer;
}
.btn {
  cursor: url('../assets/ani/link_2.png'), pointer;
}
</style>