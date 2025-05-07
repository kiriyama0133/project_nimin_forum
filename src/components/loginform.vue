<script lang="ts" setup>
import { ElMessage } from 'element-plus';
import {useCounterStore} from '../stores/login_register'
const store = useCounterStore()
import { useRouter } from 'vue-router';
import { LoginService, OpenAPI } from '../client';
import { ref } from 'vue';
OpenAPI.BASE = 'http://localhost:8000';
const router = useRouter()
let LoginData = ref({
  username: '',
  password: ''
})
function rigister() {
  store.homepage='register'
}

const LoginSend = async () => {
  store.loading = true;
  try {
    const response = await LoginService.loginAccessToken({
      formData: {
        username: LoginData.value.username,
        password: LoginData.value.password
      }
    });

    console.log('Login Successful:', response);

    if (response.access_token) {
      localStorage.setItem('access_token', response.access_token);
      OpenAPI.TOKEN = response.access_token;

      ElMessage({
        message: '登录成功',
        type: 'success',
        duration: 2000
      });

      router.push('/homepage');
    } else {
       console.error('登录失败: 未收到 access_token');
       ElMessage({
        message: '登录失败: 未收到凭证',
        type: 'error',
        duration: 3000
      });
    }

  } catch (error) {
    console.error('登录请求失败:', error);
    ElMessage({
        message: '登录失败，请检查邮箱或密码',
        type: 'error',
        duration: 3000
      });
  } finally {
    store.loading = false;
  }
};

function handle() {
  LoginSend()
}
</script>
<template>

<div class="">
    <div class="flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
    <!-- 图标 -->
    <el-icon class="text-gray-500 mr-2">
      <User />
    </el-icon>
    <!-- 输入框 -->
    <input v-model="LoginData.username"
      placeholder="请输入邮箱"
      class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
    />
    </div>

  <div class=" mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
    <!-- 图标 -->
    <el-icon class="text-gray-500 mr-2">
      <Lock />
    </el-icon>
    <!-- 输入框 -->
    <input type="password" v-model="LoginData.password"
      placeholder="请输入密码"
      class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
    />
    </div>

    <div class="flex justify-between items-center m-5">
    <!-- 登录按钮 -->
    <button @click="handle"
      class="btn w-15 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
    >
      登录
    </button>

    <!-- 注册按钮 -->
    <button @click="rigister"
      class="btn w-15 py-2 bg-gray-100 text-gray-700 font-semibold rounded-lg shadow-md hover:bg-gray-200 hover:shadow-lg transition duration-300"
    >
      注册
    </button>

    <!-- 重置密码按钮 -->
    <button @click="store.homepage='reset'"
      class="btn w-15 py-2 bg-gray-100 text-gray-700 font-semibold rounded-lg shadow-md hover:bg-gray-200 hover:shadow-lg transition duration-300"
    >
      重置
    </button>
  </div>
</div>
</template>
<style scoped>
.text {
    cursor: url('../assets/ani/text_2.png'), pointer;
}
.btn{
    cursor: url('../assets/ani/link_2.png'), pointer;
}
</style>