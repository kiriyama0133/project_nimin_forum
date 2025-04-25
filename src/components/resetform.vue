<script lang="ts" setup>
import { ref } from 'vue';
import { useCounterStore } from '../stores/login_register';

const store = useCounterStore();

function send() {
    isloading.value = true
}
const isloading = ref(false)
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
        placeholder="输入验证码"
        class="text flex-1 p-2 bg-transparent outline-none text-gray-700 placeholder-gray-400 focus:ring-2 focus:ring-blue-500 rounded-md"
      />
      <button v-if="!isloading" @click="send"
        class="btn w-18 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 hover:shadow-lg transition duration-300"
      >
        发送验证
      </button>
        <button  v-if="isloading" type="button" class="w-18" disabled>
            <svg class="mr-3 size-5 animate-spin" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/>
            </svg>
        </button>
    </div>

    <!-- 密码输入框 -->
    <div class="mt-5 flex items-center w-full p-2 bg-pink-100 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
      <el-icon class="text-gray-500 mr-2">
        <Lock />
      </el-icon>
      <input
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