<script setup lang="ts">
import { ref } from 'vue';
import 'primeicons/primeicons.css';
import Button from 'primevue/button';
import Menubar from 'primevue/menubar';
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import InputGroupAddon from 'primevue/inputgroupaddon';
import Popover from 'primevue/overlaypanel'; // Popover 实际是 OverlayPanel
const items_ = ref([
   {
       label: '主页',
       icon: 'pi pi-home'
   },
   {
       label: '搜索',
       icon: 'pi pi-search',
    },
]);

const op = ref();
const members = ref([
    { name: 'Amy Elsner', image: 'amyelsner.png', email: 'amy@email.com', role: 'Owner' },
    { name: 'Bernardo Dominic', image: 'bernardodominic.png', email: 'bernardo@email.com', role: 'Editor' },
    { name: 'Ioni Bowcher', image: 'ionibowcher.png', email: 'ioni@email.com', role: 'Viewer' }
]);
const toggle = (event:any) => {
    op.value.toggle(event);
}
</script>
<template>
<Menubar :model="items_" breakpoint="520px" :base-z-index="90">
    <template #end>
        <div class="flex items-center gap-2">
            <div class="flex gap-2">
                <Button variant="outlined" raised style="font-size: 10px;" class="text w-23 h-8" label="饼干管理" icon="pi pi-user" />
                <Button variant="outlined" raised style="font-size: 10px;" class="text w-18 h-8" label="收藏" icon="pi pi-star" />
            </div>

        <div id="user-info" class="">
            <div class="card flex justify-center">
                <Button variant="outlined" raised class="w-18 h-8" style="font-size: 10px;" type="button" icon="pi pi-user" label="用户" @click="toggle" />
                    <Popover :base-z-index="90" ref="op">
                        <div class="flex flex-col gap-4 w-[16rem]">
                            <div>
                                <span class="font-medium block mb-2">Share this document</span>
                                <InputGroup>
                                    <InputText value="https://primevue.org/12323ff26t2g243g423g234gg52hy25XADXAG3" readonly class="w-[16rem]"></InputText>
                                    <InputGroupAddon>
                                        <i class="pi pi-copy"></i>
                                    </InputGroupAddon>
                                </InputGroup>
                            </div>
                            <div>
                                <span class="font-medium block mb-2">Invite Member</span>
                                <InputGroup>
                                    <InputText disabled />
                                    <Button label="Invite" icon="pi pi-users"></Button>
                                </InputGroup>
                            </div>
                            <div>
                                <span class="font-medium block mb-2">用户</span>
                                <ul class="list-none p-0 m-0 flex flex-col gap-4">
                                    <li v-for="member in members" :key="member.name" class="flex items-center gap-2">
                                        <img :src="`https://primefaces.org/cdn/primevue/images/avatar/${member.image}`" style="width: 32px" />
                                        <div>
                                            <span class="font-medium">{{ member.name }}</span>
                                            <div class="text-sm text-surface-500 dark:text-surface-400">{{ member.email }}</div>
                                        </div>
                                        <div class="flex items-center gap-2 text-surface-500 dark:text-surface-400 ml-auto text-sm">
                                            <span>{{ member.role }}</span>
                                        </div>
                                    </li>
                                </ul>
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
</style>