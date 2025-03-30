// src/stores/userlogin.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';
export const useDrawerStore = defineStore('drawer', () => {
    let Drawervisible = ref<boolean>(false);
  return {
    Drawervisible
  };
});
