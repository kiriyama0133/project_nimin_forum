<script lang="ts" setup>
import sendcard from '../components/sendcard.vue';
import { sendcarddata } from '../types/sendcard';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import {useDialogStore} from '../stores/dialog'
const dialog = useDialogStore();
//回复模块的数据示例
let carddata_: sendcarddata[] = [
    {
    id:"Kiriyama",
    content:"你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面你好，这里是第一条发言,点击可以进入内容页面",
    thumbs:0
    },
    {
    id:"KJHKJHJ",
    reply:"Kiriyama",
    content:"你好，这里是一条回复，回复内容会被加以粉色装饰",
    thumbs:0
    },
    {
    id:"Kiriyama",
    content:"你好",
    thumbs:0
    },
    {
    id:"Kiriyama",
    content:"你好",
    thumbs:0
    },   
]
</script>
<template>
    <div class="card flex justify-center">
        <Dialog v-model:visible="dialog.Dialogvisible" modal header="回复" :style="{ width: '25rem' }">
            <div class="flex items-center gap-4 mb-4">
                <label for="username" class="font-semibold w-24">回复的用户</label>
                <p>{{ dialog.replyuser }}</p>
            </div>
            <div class="flex items-center gap-4 mb-8">
                <InputText id="email" class="flex-auto" autocomplete="off"></InputText>   
            </div>
            <div class="flex justify-end gap-2">
                <Button type="button" label="取消" severity="secondary" @click="dialog.Dialogvisible = false"></Button>
                <Button type="button" label="发送" @click="dialog.Dialogvisible = false"></Button>
            </div>
        </Dialog>
    </div>
    <div class="flex flex-col gap-1">
        <sendcard v-for="(item,i) in carddata_"
            :id="item.id"
            :index="i+1"
            :reply="item.reply"
            :content="item.content"
            :thumbs="item.thumbs"
        >
    </sendcard>
    </div>
    <div class="h-30 flex justify-center items-center">
        没有更多内容了~
    </div>   
</template>
<style>
input{
    cursor: url('../assets/ani/text_2.png'), pointer;    
}
</style>