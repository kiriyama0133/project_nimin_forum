<script setup lang="ts">
import { ref } from 'vue';
import 'primeicons/primeicons.css';
import Menu from 'primevue/menu';
import axiosInstance from '../utils/getCards'
import {useCarddata} from '../stores/carddata'
import { useRouter } from 'vue-router';
const cardstore = useCarddata()
const router = useRouter()
import PanelMenu from 'primevue/panelmenu';

// 修复点：通过 .value 修改 ref 对象的值
function refresh(path:string,api:string) {
    cardstore.carddata.splice(0,cardstore.carddata.length); //清空列表
    router.push(path);
    axiosInstance.get(api).then((response)=>{
        cardstore.carddata.push(response.data)
    })

}
const items = ref([
    {
        label: '分类',
        items: [
            {
                label: '综合板',
                icon: 'pi pi-plus',
                command:()=>{
                    router.push('/Classification/total')
                }
            },
            {
                label: '时间板',
                icon: 'pi pi-search',
                command:()=>{
                    router.push('/Classification/time')
                }
            }
        ]
    },
    {
        label: '亚文化',
        items: [
            {
                label: '婆罗门',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '漫画',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '动画',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '电影/电视剧',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: 'vtuber',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '卡牌桌游',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '特摄',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '战锤',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '胶佬',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '铁道厨',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: 'VOCALOID',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '东方project',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
            },
            {
                label: '舰娘',
                icon: 'pi pi-cog',
                command:()=>{
                    refresh('/subculture','/getcard')
                }
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
    label: '生活',
    items: [
        {
            label: '露营',
            icon: 'pi pi-cog'
        },
        {
            label: '自救互助',
            icon: 'pi pi-cog'
        },
        {
            label: '料理',
            icon: 'pi pi-cog'
        },
        {
            label: '体育',
            icon: 'pi pi-cog'
        },
        {
            label: '学业',
            icon: 'pi pi-cog'
        },
        {
            label: '日记',
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
<style scoped>
</style>