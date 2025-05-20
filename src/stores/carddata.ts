// src/stores/carddata.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';
import type{carddata} from '../types/carddata'
import type{DefaultCard,AddReplyCard} from '../types/sendcard.d'
export const useCarddata = defineStore('card', () => {
    let carddata = ref<carddata[]>([]);
    let category = ref<string>(''); 
    let UserCard = {
      defaultcard: ref<DefaultCard[]>([]),
      addreplycard: ref<AddReplyCard[]>([]),
    }
  return {
    carddata,
    category,
    UserCard
  };
});