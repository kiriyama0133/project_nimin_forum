<script setup lang="ts">
import registerform from '../Forms/registerform.vue';
import gsap from "gsap";
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
gsap.registerPlugin(MotionPathPlugin);
</script>

<template>
    <div class="register col-span-3 w-full font-mono p-10">
        <div class="grid grid-rows-8 ">
            <!-- 标题 -->
            <div class="row-span-1 h-full">
                <p class="select-none text-2xl text-gray-700 font-extrabold text-center">
                    SWPU匿名论坛
                </p>
            </div>

            <!-- 注册表单 -->
            <div class="row-span-5 h-full">
                <registerform>
                </registerform>
            </div>

            <!-- 底部信息 -->
            <div class="row-span-1 h-full w-full text-center mt-10">
                <p>Disigned by Kiriyama</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* 可根据需要添加自定义样式 */
</style>