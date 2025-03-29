<script setup lang="ts">
import loginform from '../components/loginform.vue';
import gsap from "gsap";
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
gsap.registerPlugin(MotionPathPlugin);

</script>
<template>
    <div class="login col-span-3 w-full font-mono p-10">
        <div class="grid grid-rows-5 gap-2">
            <div class=" row-span-1 h-full">
                <p class=" select-none text-2xl text-gray-700 font-extrabold text-center">
                    SWPU匿名论坛
                </p>
            </div>
            <div class="row-span-2 h-full">
                <loginform>
                </loginform>
            </div>

            <div class="row-span-2 h-full w-full text-center mt-[10vh]">
                <p>Disigned by Kiriyama</p>
            </div>
            </div>
        </div>
</template>

<style scoped>

</style>