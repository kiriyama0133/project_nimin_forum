// src/stores/userlogin.ts
import { defineStore } from 'pinia';
import { ref } from 'vue';
export const useDialogStore = defineStore('drawer', () => {
    let Dialogvisible = ref<boolean>(false);
    let replyuser = ref<string>("");
  return {
    Dialogvisible,
    replyuser
  };
});