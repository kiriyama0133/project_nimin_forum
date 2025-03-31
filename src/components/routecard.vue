<script setup lang="ts">
function Hi(){
    console.log("hello there")
}
</script>
<template>
    <div @click="Hi" class="mx-auto flex max-w-xs items-center gap-x-2 rounded-xl bg-white p-6 
    shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none 
    dark:-outline-offset-1 dark:outline-white/10" style="height: 50px;width: 160px;">
        <div>
            <slot name="header">
                <img class="size-6 shrink-0" src="../assets/bg/icons8.gif" alt="ChitChat Logo" />
            </slot>
        </div>
        <div>
            <div name="head" class="text-xs font-extrabold text-black dark:text-white font-mono">
                <slot name="head">新的回复</slot>
            </div>
                <p name="content" class="text-gray-500 dark:text-gray-400 text-xs">
                    <slot name="content">你好！世界！</slot>
                </p>
        </div>
    </div>
</template>
<style>
</style>