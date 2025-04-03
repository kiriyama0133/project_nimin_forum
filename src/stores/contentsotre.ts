// src/stores/contentsotre.ts 此页用来动态管理显示的回复数据 
//清空请使用 sotre.carddata.splice(0,cardstore.carddata.length); //清空列表
import { defineStore } from 'pinia';
import { ref } from 'vue';
import type{ sendcarddata } from '../types/sendcard';
export const useCarddata = defineStore('card', () => {
    let contentdata = ref<sendcarddata[]>([]);
  return {
    contentdata
  };
});