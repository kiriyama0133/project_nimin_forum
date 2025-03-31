<script setup lang="ts">
import subcltureheader from '../../components/subcltureheader.vue';
import defaultcard from '../../components/defaultcard.vue';
import type { carddata } from '../../types/carddata';
//这里写一个示例的卡片传入参数的数据格式：
let carddata_: carddata[] = [
    {
    number:1,
    id:"Kiriyama",
    content:"你好，这里是第一条发言,点击可以进入内容页面"
    },
    {
    number:2,
    id:"Kiriyama",
    content:"你好"
    },
    {
    number:3,
    id:"Kiriyama",
    content:"你好"
    },
    {
    number:3,
    id:"Kiriyama",
    content:"你好"
    },   
]

</script>
<template>
    <div class="subculture h-full">
        <div name="header">
            <subcltureheader>
                <template #header>
                    <!-- 如果不适用插槽则显示默认内容,这里打算用v-html去渲染内容，由接口服务 -->
                </template>
            </subcltureheader>
        </div>

        <div name="content" class="flex flex-col gap-2">
            <defaultcard v-for="item in carddata_"
                :number="item.number"
                :id="item.id"
                :content="item.content"
            >
            </defaultcard>
        </div>
    </div>
    <div class="h-100 flex">
    </div> 
</template>
<style scoped>
.subculture{
cursor: url('@/assets/ani/select_2.png'), pointer;
}
</style>