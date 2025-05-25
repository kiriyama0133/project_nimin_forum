<template>
    <div class="flex flex-col gap-4">
        <RouteCard  v-for="card in cardstore.UserCard.defaultcard"
        :number="card.number"
        :id="card.id"
        :content="card.content"
        :time="card.time"
        :imageUrls="card.imageUrls"
        >
        </RouteCard>
        <RouteCard v-for="card in cardstore.UserCard.addreplycard"
        :number="card.number"
        :id="card.id"
        :content="card.content"
        :time="card.time"
        :thumbs="card.thumbs"
        :number_primary="card.number_primary"
        :imageUrls="card.imageUrls"
        />
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useCarddata } from '@/stores/carddata';
import { isloading } from '@/stores/isloading';
import { useInfiniteScroll } from '@/utils/infiniteScroll';
import RouteCard from '@/components/Cards/RouteCard.vue';

const cardstore = useCarddata();
const isloadingstore = isloading();
const dataloading = ref(false);
const scrollContainer = ref<HTMLElement | null>(null);

// 这里初始化滚动加载
const { handleScroll, loadMore } = useInfiniteScroll({
  scrollContainer,
  dataloading,
  cardstore,
  isloadingstore
});

console.log(cardstore.UserCard);
</script>

<style scoped>
.scroll-container {
  height: 100%;
  overflow-y: auto;
}
</style>

