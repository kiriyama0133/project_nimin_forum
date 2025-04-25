<script lang="ts" setup>
import { useCounterStore } from '../stores/login_register';
const store = useCounterStore();

function register() {
  console.log('注册表单提交');
  // 在这里可以添加注册逻辑，例如表单验证或 API 调用
}
</script>

<template>
  

  <div class="">
    <!-- 昵称输入框 -->

    <!-- 邮箱输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Message />
      </el-icon>
      <input
        type="email"
        placeholder="请输入邮箱"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
      <button
        @click="register"
        class="btn w-18 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
      >
        发送验证
      </button>
    </div>

    <!-- 密码输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Lock />
      </el-icon>
      <input
        type="password"
        placeholder="请输入密码"
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
        placeholder="请确认密码"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
    </div>

    <!-- 按钮 -->
    <div class="flex justify-between items-center m-5">
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