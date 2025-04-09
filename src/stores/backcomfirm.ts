import { defineStore } from 'pinia';
import { ref } from 'vue';
import type{BackComfirm} from '../types/backcomfirm'
export const getBackComfirm = defineStore('backmessage', () => {
    let BackComfirm = ref<BackComfirm>({
        message: '',
    }
    );
  return {
    BackComfirm
  };
});