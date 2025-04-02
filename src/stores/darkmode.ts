// src/stores/darkmode.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';
export const useDarkmode = defineStore('darkmode', () => {
    let Darkmode = ref<boolean>(false);
  return {
    Darkmode
  };
});