<script lang="ts" setup>
import  Button  from 'primevue/button';
import { useDrawerStore} from '../stores/drawer'
const drawerStore = useDrawerStore()
function drawer() {
    drawerStore.Drawervisible = true
}
</script>
<template>
    <div class="mx-auto h-[600px] flex justify-center items-center gap-x-10 rounded-xl bg-white p-2 shadow-2xl outline outline-black/5
     dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">
        <img class="size-30 shrink-0 object-cover max-h-50" src="../assets/bg/defalut.jpg" alt="ChitChat Logo" />
        <div>
            <div class="text-xl font-extrabold text-black dark:text-white text-center">鸣谢</div>
            <p class="text-gray-500 dark:text-gray-400 text-center font-mono">这里是开发者们</p>
            <p class="text-gray-500 dark:text-gray-400 text-center font-mono">祝愿你有美好的一天!</p>
        </div>
        <Button icon="pi pi-arrow-right" @click="drawer" />
    </div>
</template>