import { defineStore } from 'pinia';
import { ref } from 'vue';

export const isloading = defineStore('islogin', () => {
    let dataloading = ref(false);
    let dataend = ref(false);
    let currentItemCount = ref(0);

    const resetLoadingState = () => {
        dataloading.value = false;
        dataend.value = false;
        currentItemCount.value = 0;
        console.log("Loading state reset via function.");
    };

    return {
        dataloading,
        dataend,
        currentItemCount,
        resetLoadingState
    };
});