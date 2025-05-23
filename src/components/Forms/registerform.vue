<script lang="ts" setup>
import { ElMessage } from 'element-plus';
import { useCounterStore } from '../../stores/login_register';
import { UsersService } from '../../client';
import { ref } from 'vue';
import type { UserRegister } from '../../client';
import { isloading } from '../../stores/isloading';
import loadinganime from '../Common/loadinganime.vue';
import axiosInstance from '../../utils/getCode';
import countsecond from '../Common/countsecond.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const isloadingStore = isloading();
const store = useCounterStore();
const isCounting = ref(false);

// 获取当前URL
console.log('当前路由路径:', route.path);
console.log('当前完整URL:', window.location.href);

function goToLogin() {
  store.homepage = 'login';
}
let RegisterData = ref<UserRegister>({
  email: '',
  verify_code: '',
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
   if (!RegisterData.value.verify_code.length) {
    ElMessage({
      message: '请输入验证码',
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

// 发送验证码
async function sendcode() {
  if (!RegisterData.value.email) {
    ElMessage({
      message: '请输入邮箱',
      type: 'warning',
      duration: 2000
    });
    return;
  }
  isloadingStore.loginloading = true;
  try {
    const response = await axiosInstance.post('/get_verify_code', {
      email: RegisterData.value.email
    });
    if (response.status === 200) {
      ElMessage({
        message: '验证码发送成功',
        type: 'success',
        duration: 2000
      });
      isCounting.value = true;
    } else {
      ElMessage({
        message: '验证码发送失败',
        type: 'error',
        duration: 2000
      });
    }
  } catch (error) {
    console.log(error);
    ElMessage({
      message: '验证码发送失败',
      type: 'error',
      duration: 2000
    });
  } finally {
    isloadingStore.loginloading = false;
  }
}

const handleCountdownEnd = () => {
  isCounting.value = false;
};

// 注册
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

    <div class="flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 mb-5">
      <el-icon class="text-gray-500 mr-2">
        <Lock />
      </el-icon>
      <input
        v-model="RegisterData.verify_code"
        placeholder="输入验证码"
        class="text w-20 flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
      <button v-if="!isloadingStore.loginloading && !isCounting" @click="sendcode"
        class="btn whitespace-nowrap px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
      >
        <span>发送验证</span>
      </button>
      <countsecond v-if="isCounting" :start-count="true" @countdown-end="handleCountdownEnd" />
      <loadinganime v-if="isloadingStore.loginloading"></loadinganime>
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