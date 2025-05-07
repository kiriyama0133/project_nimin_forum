<script setup lang="ts">
import { ref } from 'vue';
import 'primeicons/primeicons.css';
import Menu from 'primevue/menu';
import axiosInstance from '../utils/getCards'
import {useCarddata} from '../stores/carddata'
import { useRouter } from 'vue-router';
import { getBackComfirm } from '../stores/backcomfirm';
import { useToast } from "primevue/usetoast";
const getbackcomfirm = getBackComfirm()
const cardstore = useCarddata()
const router = useRouter()
const visible = ref(false);
const toast = useToast()
const suggest = ref('')
const email = ref('')
import Dialog from 'primevue/dialog';
import PanelMenu from 'primevue/panelmenu';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import axiosComfirm from '../utils/comfirm'
import { isloading } from '../stores/isloading';
const isloadingstore = isloading();
//动态去得到对应的内容的卡片，并且刷新页面
function refresh(path: string, api: string, category: string) {
    console.log(`刷新分类: ${category}, 路径: ${path}, API: ${api}`);
    cardstore.carddata.splice(0, cardstore.carddata.length); // 清空列表
    isloadingstore.dataloading = true;
    cardstore.category = category;//设置分类
    //console.log("当前的分类是：",cardstore.category)
    router.push(path);
    isloadingstore.dataend = false;
    //第一次加载内容
    axiosInstance.post(api, { skip: 0, category: category }).then((response) => {
        const receivedCards = response.data.data;
        if (receivedCards && Array.isArray(receivedCards)) {
            cardstore.carddata.push(...receivedCards);
            console.log(`分类 "${category}" 的初始卡片数据已加载:`, cardstore.carddata);
            if (cardstore.carddata.length === 0) {
                isloadingstore.dataend = true;
            }
        } else {
            console.warn(`分类 "${category}" 返回的初始卡片数据无效或为空:`, receivedCards);
            // Handle case where category might have no cards initially
        }
    }).catch(error => {
        console.error(`从 ${api} (分类: ${category}) 刷新初始数据失败:`, error);
        toast.add({ severity: "error", summary: "错误", detail: "加载初始数据失败", life: 3000 });
    }).finally(() => {
        // cardstore.initialLoading = false; // Reset loading state if used
    });
}
const backComfirm = async () => {
    getbackcomfirm.BackComfirm.message=''; // 清空之前的卡片数据
    if (!suggest.value.trim() || !email.value.trim()) {
  toast.add({severity: "warn",summary: "提醒",detail: "请填写完整的反馈内容和邮箱！",life: 3000});
    return;
    }
    try {
        //发送数据到后端并返回后端的反馈
    const response = await axiosComfirm.post('/send',{
        suggest:suggest.value,
        email:email.value,
    });
    console.log('Registration Successful:', response);
    console.log('目前已得到的卡片数据：', response.data);
    toast.add({ severity: "success", summary: "成功", detail: response.data.message, life: 3000 });
    suggest.value = ''; // 清空输入框
    email.value = ''; // 清空输入框
    }catch (error) {
    console.error('请求失败:', error);
    toast.add({ severity: "error", summary: "错误", detail: error, life: 3000 });
}
};
const sendmessageToadmin =()=> {
    setTimeout(() => {
    backComfirm().then(()=>{
        console.log("数据加载完毕")
        visible.value = false;
       
 }); 
  }, 1000);
};
const buttonclick=() => {
    console.log("点击了发送按钮")
    sendmessageToadmin()
};

const items = ref([
    {
        label: '分类',
        items: [
            {
                label: '综合板',
                icon: 'pi pi-plus',
                command: () => { refresh('/total', '/getcard', 'total') }
            },
            {
                label: '时间板',
                icon: 'pi pi-search',
                command: () => { refresh('/time', '/getcard', 'time') }
            }
        ]
    },
    {
        label: '亚文化',
        items: [
            {
                label: '婆罗门',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'brahmin') }
            },
            {
                label: '动漫',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'anime') }
            },
            {
                label: '电影/电视剧',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'movie_tv') }
            },
            {
                label: 'vtuber',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'vtuber') }
            },
            {
                label: '卡牌桌游',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'boardgame') }
            },
            {
                label: '特摄',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'tokusatsu') }
            },
            {
                label: '战锤',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'warhammer') }
            },
            {
                label: '胶佬',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'modelkit') }
            },
            {
                label: '铁道厨',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'railfan') }
            },
            {
                label: 'VOCALOID',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'vocaloid') }
            },
            {
                label: '东方project',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'touhou') }
            },
            {
                label: '舰娘',
                icon: 'pi pi-cog',
                command: () => { refresh('/subculture', '/getcard', 'kancolle') }
            },
        ]
    },
    {
    label: '创作',
    items: [
        {
            label: '跑团',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'trpg') }
        },
        {
            label: '创作',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'creation') }
        },
        {
            label: '规则怪谈',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'creepypasta') }
        },
        {
            label: '海龟汤',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'situation_puzzle') }
        },
        {
            label: '科学',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'science') }
        },
        {
            label: '文学',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'literature') }
        },
        {
            label: '音乐',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'music') }
        },
        {
            label: 'AI',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'ai') }
        },
        {
            label: '摄影',
            icon: 'pi pi-cog',
            command: () => { refresh('/create', '/getcard', 'photography') }
        },
        ]
    },
    {
    label: '游戏',
    items: [
        {
            label: '综合',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'game_general') }
        },
        {
            label: '手游',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'mobile_game') }
        },
        {
            label: '任天堂',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'nintendo') }
        },
        {
            label: 'Galgame',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'galgame') }
        },
        {
            label: '暴雪游戏',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'blizzard') }
        },
        {
            label: 'SE',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'square_enix') }
        },
        {
            label: 'V社',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'valve') }
        },
        {
            label: '怪物猎人',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'monster_hunter') }
        },
        {
            label: '鹰角',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'hypergryph') }
        },
        {
            label: '米哈游',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'mihoyo') }
        },
        {
            label: '音游',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'rhythm_game') }
        },
        {
            label: '腾讯游戏',
            icon: 'pi pi-cog',
            command: () => { refresh('/game', '/getcard', 'tencent_game') }
        },
        ]
    },
    {
    label: '生活',
    items: [
        {
            label: '露营',
            icon: 'pi pi-cog',
            command: () => { refresh('/life', '/getcard', 'camping') }
        },
        {
            label: '自救互助',
            icon: 'pi pi-cog',
            command: () => { refresh('/life', '/getcard', 'self_help') }
        },
        {
            label: '料理',
            icon: 'pi pi-cog',
            command: () => { refresh('/life', '/getcard', 'cooking') }
        },
        {
            label: '体育',
            icon: 'pi pi-cog',
            command: () => { refresh('/life', '/getcard', 'sports') }
        },
        {
            label: '学业',
            icon: 'pi pi-cog',
            command: () => { refresh('/life', '/getcard', 'study') }
        },
        {
            label: '日记',
            icon: 'pi pi-cog',
            command: () => { refresh('/life', '/getcard', 'diary') }
        },
        ]
    },
    {
        label: '联系管理员',
        icon: 'pi pi-envelope',
        command: () => { visible.value = true }
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
<Dialog v-model:visible="visible" modal header="联系管理员" class="justyfy-content-center h-150">
    <span class="text-surface-500 dark:text-surface-400 block mb-8 ">提交你的建议和报告bug</span>
    <div class=" card flex items-center gap-4 mb-4">
        <FloatLabel>
            <Textarea v-model="suggest" id="over_label" class="w-90 resize-none"   rows="12" />
            <label>写下你的建议吧</label>
        </FloatLabel>
    </div>
    <div class="flex items-center gap-4 mb-8">
        <label for="email" class="font-semibold ">你的邮件</label>
        <InputText v-model="email" id="email" class="flex-auto " autocomplete="off" />
    </div>
    <div class="flex justify-end gap-2">
        <Button type="button" label="取消" severity="secondary" @click="visible = false"></Button>
        <div class="card flex justify-center">
            <Button type="button" label="发送" @click="buttonclick()"/>
        </div>
    </div>
</Dialog>
<div class="h-12"></div>
</template>
<style scoped>
</style>