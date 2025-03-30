<script setup lang="ts">
import { ref } from 'vue';
import 'primeicons/primeicons.css';
import Menu from 'primevue/menu';
import PanelMenu from 'primevue/panelmenu';
const items = ref([
    {
        label: '分类',
        items: [
            {
                label: '综合板',
                icon: 'pi pi-plus'
            },
            {
                label: '时间板',
                icon: 'pi pi-search'
            }
        ]
    },
    {
        label: '亚文化',
        items: [
            {
                label: '婆罗门',
                icon: 'pi pi-cog'
            },
            {
                label: '漫画',
                icon: 'pi pi-cog'
            },
            {
                label: '动画',
                icon: 'pi pi-cog'
            },
            {
                label: '电影/电视剧',
                icon: 'pi pi-cog'
            },
            {
                label: 'vtuber',
                icon: 'pi pi-cog'
            },
            {
                label: '卡牌桌游',
                icon: 'pi pi-cog'
            },
            {
                label: '特摄',
                icon: 'pi pi-cog'
            },
            {
                label: '战锤',
                icon: 'pi pi-cog'
            },
            {
                label: '胶佬',
                icon: 'pi pi-cog'
            },
            {
                label: '铁道厨',
                icon: 'pi pi-cog'
            },
            {
                label: 'VOCALOID',
                icon: 'pi pi-cog'
            },
            {
                label: '东方project',
                icon: 'pi pi-cog'
            },
            {
                label: '舰娘',
                icon: 'pi pi-cog'
            },
        ]
    },
    {
    label: '创作',
    items: [
        {
            label: '跑团',
            icon: 'pi pi-cog'
        },
        {
            label: '创作',
            icon: 'pi pi-cog'
        },
        {
            label: '规则怪谈',
            icon: 'pi pi-cog'
        },
        {
            label: '海龟汤',
            icon: 'pi pi-cog'
        },
        {
            label: '科学',
            icon: 'pi pi-cog'
        },
        {
            label: '文学',
            icon: 'pi pi-cog'
        },
        {
            label: '音乐',
            icon: 'pi pi-cog'
        },
        {
            label: 'AI',
            icon: 'pi pi-cog'
        },
        {
            label: '摄影',
            icon: 'pi pi-cog'
        },
        ]
    },
    {
    label: '游戏',
    items: [
        {
            label: '综合',
            icon: 'pi pi-cog'
        },
        {
            label: '手游',
            icon: 'pi pi-cog'
        },
        {
            label: '任天堂',
            icon: 'pi pi-cog'
        },
        {
            label: 'Galgame',
            icon: 'pi pi-cog'
        },
        {
            label: '暴雪游戏',
            icon: 'pi pi-cog'
        },
        {
            label: 'SE',
            icon: 'pi pi-cog'
        },
        {
            label: 'V社',
            icon: 'pi pi-cog'
        },
        {
            label: '怪物猎人',
            icon: 'pi pi-cog'
        },
        {
            label: '鹰角',
            icon: 'pi pi-cog'
        },
        {
            label: '米哈游',
            icon: 'pi pi-cog'
        },
        {
            label: '音游',
            icon: 'pi pi-cog'
        },
        {
            label: '腾讯游戏',
            icon: 'pi pi-cog'
        },
        ]
    },
    {
    label: '应用设置',
    icon: 'pi pi-cog'
    },
    {
        label: '联系管理员',
        icon: 'pi pi-envelope'
    }
]);
</script>
<template>
<Menu class="w-40 overflow-x-hidden">
    <template #start> 
        <div class="card flex justify-center">
            <PanelMenu :model="items" class="w-full md:w-80" />
        </div>
    </template>
</Menu> 
<div class="h-12"></div>
</template>