// src/stores/carddata.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';
import type{carddata} from '../types/carddata'
export const useCarddata = defineStore('card', () => {
    let carddata = ref<carddata[]>([]);
    let category = ref<string>(''); 
  return {
    carddata,
    category
  };
});