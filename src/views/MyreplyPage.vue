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
import { useCarddata } from '@/stores/carddata';
import RouteCard from '@/components/Cards/RouteCard.vue';
const cardstore = useCarddata();
console.log(cardstore.UserCard);
</script>

