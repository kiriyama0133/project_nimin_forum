<script lang="ts" setup>
import { useCounterStore } from '../../stores/login_register';
import { isloading } from '../../stores/isloading';
const isloadingStore = isloading();
import loadinganime from '../Common/loadinganime.vue';
import { ElMessage } from 'element-plus';
import type{Resetquest} from '../../types/logins/reset';
import { ref } from 'vue';
import axiosInstance from '../../utils/getCode';
import axiosInstance_user from '../../utils/users';
const store = useCounterStore();
const isCounting = ref(false);
let ResetData = ref<Resetquest>({
  email: '',
  verify_code: '',
  password: ''
});
// 重设密码
async function reset() {
  if (!ResetData.value.email || !ResetData.value.verify_code || !ResetData.value.password) {
    ElMessage({
      message: '请输入邮箱、验证码和密码',
      type: 'warning',
      duration: 2000
    });
    return;
  }   
  if (ResetData.value.password.length < 8) {
    ElMessage({
      message: '密码长度不能少于8位',
      type: 'warning',
      duration: 2000
    });
    return;
  }
  isloadingStore.loginloading = true;
  try {
    const response = await axiosInstance_user.post('/reset_password', {
      email: ResetData.value.email,
      verify_code: ResetData.value.verify_code,
      password: ResetData.value.password
    });
    if (response.status === 200) {
      ElMessage({
        message: '重设密码成功',
        type: 'success',
        duration: 2000
      });
      ResetData.value = { // 重置输入框
        email: '',
        verify_code: '',
        password: ''
      };
      store.homepage = 'login';
    } else {
      ElMessage({
        message: '重设密码失败',
        type: 'error',
        duration: 2000
      });
    }
  } catch (error) {
    console.log(error);
    ElMessage({
      message: '重设密码失败',
      type: 'error',
      duration: 2000
    });
  } finally {
    isloadingStore.loginloading = false;
  }
}

// 发送验证码
async function send() {
  if (!ResetData.value.email) {
    ElMessage({
      message: '请输入邮箱',
      type: 'warning',
      duration: 2000
    });
    return;
  }
  isloadingStore.loginloading = true;
  try {
    const response = await axiosInstance.post('/reset_password_verify_code', {
      email: ResetData.value.email
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
</script>

<template>
  <div class="transition-all">
    <!-- 昵称输入框 -->
    <!-- 邮箱输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Message />
      </el-icon>
      <input
        v-model="ResetData.email"
        type="email"
        placeholder="请输入邮箱"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />

    </div>
    <!-- 验证码输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Lock />
      </el-icon>
      <input
        v-model="ResetData.verify_code"
        placeholder="输入验证码"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
      <button v-if="!isloadingStore.loginloading" @click="send"
        class="btn w-18 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
      >
        发送验证
      </button>
        <loadinganime></loadinganime>
    </div>

    <!-- 密码输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Lock />
      </el-icon>
      <input
        v-model="ResetData.password"
        type="password"
        placeholder="新的密码"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
    </div>

    <!-- 确认密码输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Lock />
      </el-icon>
      <input
        type="password"
        placeholder="确认新的密码"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
    </div>

    <!-- 按钮 -->
    <div class="flex justify-between items-center m-5">

      <!-- 重设密码按钮 -->
      <button 
        @click="reset"
        class="btn w-20 py-2 bg-green-500 text-white font-semibold rounded-lg shadow-md hover:bg-green-600 hover:shadow-lg transition duration-300"
      >
        重设密码
      </button>

      <!-- 提交注册按钮 -->
      <button
        @click="store.homepage = 'register'"
        class="btn w-20 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
      >
        返回注册
      </button>

      <!-- 返回登录按钮 -->
      <button 
        @click="store.homepage = 'login'"
        class="btn w-20 py-2 bg-gray-100 text-gray-700 font-semibold rounded-lg shadow-md hover:bg-gray-200 hover:shadow-lg transition duration-300"
      >
        返回登录
      </button>
    </div>
  </div>
</template>

<style scoped>
.text {
  cursor: url('../assets/ani/text.png'), pointer;
}
.btn {
  cursor: url('../assets/ani/link.png'), pointer;
}
</style>