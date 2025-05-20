<script setup lang="ts">
import defaultcard from '@/components/Cards/defaultcard.vue';
import { ref, watch } from 'vue'
import type { DefaultCard, SearchCardRequest} from '@/types/sendcard.d';
import { useRequest } from 'vue-hooks-plus'
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
import { searchCard } from '@/utils/getCards';
import { ElMessage } from 'element-plus';

const search = ref('');
const searchResults = ref<DefaultCard[]>([]);
///////////依赖库导入END///////////

// 使用 useRequest 处理搜索
const { run, loading, error } = useRequest(
    async () => {
        const request: SearchCardRequest = {
            content: search.value,
            skip: 0
        };
        const result = await searchCard(request);
        if (Array.isArray(result)) {
            searchResults.value = result;  // 直接赋值而不是追加
        } else {
            searchResults.value = [];  // 如果不是数组，设置为空数组
        }
        console.log("搜索结果:", searchResults.value);
        return result;
    },
    {
        debounceWait: 500,
        manual: true,
        onSuccess: (result) => {
            console.log("搜索成功:", result);
        },
        onError: (error) => {
            console.error('搜索失败:', error);
            ElMessage({
                message: '搜索失败，请稍后重试',
                type: 'error',
                duration: 2000
            });
        }
    }
);

// 监听输入变化
watch(search, (newValue) => {
    if (newValue.trim()) {
        run();
    } else {
        searchResults.value = [];
    }
});

</script>
<template>
    <div class="w-full">
        <IconField>
            <InputIcon>
                <i class="pi pi-search" />
            </InputIcon>
            <InputText placeholder="Search" class="w-full" v-model="search"/>
        </IconField>

        <!-- 加载状态 -->
        <div v-if="loading" class="mt-4 text-center">
            <div class="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto"></div>
            <p class="mt-2 text-gray-600">搜索中...</p>
        </div>

        <!-- 错误提示 -->
        <div v-if="error" class="mt-4 text-center text-red-500">
            {{ error.message }}
        </div>

        <!-- 搜索结果 -->
        <div v-if="searchResults.length > 0" class="mt-4 flex flex-col gap-4">
            <span>搜索结果</span>
            <defaultcard
                v-for="card in searchResults"
                :key="card.number"
                :number="card.number"
                :id="card.id"
                :content="card.content"
                :time="card.time"
                :imageUrls="card.imageUrls"
                :category="card.category"
            />
        </div>

        <!-- 无结果提示 -->
        <div v-if="search && !loading && searchResults.length === 0" class="mt-4 text-center text-gray-500">
            没有找到相关结果
        </div>
    </div>
</template>
