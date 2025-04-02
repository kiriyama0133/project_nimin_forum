<script setup lang="ts">
import { ref } from 'vue';
import 'primeicons/primeicons.css';
import Button from 'primevue/button';
import Menubar from 'primevue/menubar';
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import InputGroupAddon from 'primevue/inputgroupaddon';
import Popover from 'primevue/overlaypanel'; // Popover 实际是 OverlayPanel
<<<<<<< HEAD
import { useRouter } from 'vue-router';
const router = useRouter()
=======
import ToggleSwitch from 'primevue/toggleswitch';
import { useRouter } from 'vue-router';
const router = useRouter()
const checked = ref(false);
>>>>>>> 4ffbd9549bee8820806b1b738bea23d66564efa0
const items_ = ref([
   {
       label: '主页',
       icon: 'pi pi-home',
       command:()=>{
        router.push('/Introduction')
    }
       icon: 'pi pi-home',
       command:()=>{
        router.push('/Introduction')
    }
   },
   {
       label: '搜索',
       icon: 'pi pi-search',
    },
]);

const op = ref();
const toggle = (event:any) => {
    op.value.toggle(event);
}
function toggleDarkMode() {
    document.documentElement.classList.toggle('darkmode');
}
</script>
<template>
<Menubar :model="items_" breakpoint="520px" :base-z-index="90">
  
    <template #end>
        <div class="flex items-center gap-2">
<<<<<<< HEAD
            <div class="flex gap-2">
=======
            <div class="flex gap-2 items-center">
                
                    <ToggleSwitch v-model="checked" @click="toggleDarkMode()">
                        <template #handle="{ checked }">
                <i :class="['!text-xs pi', { 'pi-moon': checked, 'pi-sun': !checked }]" />
            </template>
        </ToggleSwitch>
            
>>>>>>> 4ffbd9549bee8820806b1b738bea23d66564efa0
                <Button  :pt="{
                    root:{class: 'btn-cursor'},
                }" variant="outlined" raised style="font-size: 10px;" class="text w-18 h-8" label="收藏" icon="pi pi-star" />
                <Button :pt="{
                    root:{class: 'btn-cursor'}
                }" variant="outlined" raised style="font-size: 10px;" class="text w-23 h-8" label="饼干管理" icon="pi pi-user" />
            </div>

        <div id="user-info" class="">
            <div class="card flex justify-center">
                <Button :pt="{
                    root:{class: 'btn-cursor'}
                }" variant="outlined" raised class="w-18 h-8" style="font-size: 10px;" type="button" icon="pi pi-user" label="用户" @click="toggle" />
                <Button :pt="{
                    root:{class: 'btn-cursor'}
                }" variant="outlined" raised class="w-18 h-8" style="font-size: 10px;" type="button" icon="pi pi-user" label="用户" @click="toggle" />
                    <Popover :base-z-index="90" ref="op">
                        <div class="flex flex-col gap-1 w-[16rem]">
                        <div class="flex flex-col gap-1 w-[16rem]">
                            <div>
                                <span class="font-medium block mb-2">分享这个贴</span>
                                <span class="font-medium block mb-2">分享这个贴</span>
                                <InputGroup>
                                    <InputText value="https://primevue.org/12323ff26t2g243g423g234gg52hy25XADXAG3" readonly class="w-[16rem]"></InputText>
                                    <InputGroupAddon>
                                        <i class="pi pi-copy"></i>
                                    </InputGroupAddon>
                                </InputGroup>
                            </div>
                            <div>
                            </div>
                            <div>
                                <span class="font-medium block mb-2">用户</span>
                                <div class="flex flex-col justity-center gap-2 items-center">
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的回复" icon="pi pi-star" />
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的收藏" icon="pi pi-star" />
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的账号" icon="pi pi-star" />
                                </div>
                                <div class="flex flex-col justity-center gap-2 items-center">
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的回复" icon="pi pi-star" />
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的收藏" icon="pi pi-star" />
                                    <Button variant="outlined" 
                                    raised style="font-size: 16px;" class="text w-30 h-8" 
                                    label="我的账号" icon="pi pi-star" />
                                </div>
                            </div>
                        </div>
                    </Popover>
                </div>
            </div>
        </div>
    </template>
</Menubar>
</template>
<style>
.text{
    font-size: 20px;
}
.btn-cursor {
cursor: url('../assets/ani/link_2.png'), pointer;
}
.p-button, .p-button * {
  cursor: url('@/assets/ani/link_2.png'), pointer !important;
}
.btn-cursor {
cursor: url('../assets/ani/link_2.png'), pointer;
}
.p-button, .p-button * {
  cursor: url('@/assets/ani/link_2.png'), pointer !important;
}
</style>