<script setup lang="ts">
import { ref, onUnmounted, onMounted } from 'vue';

const props = defineProps<{
  startCount: boolean;
}>();

const emit = defineEmits<{
  (e: 'countdownEnd'): void;
}>();

const seconds = ref(60);
let timer: number | null = null;

const startCountdown = () => {
  seconds.value = 60;
  if (timer) {
    clearInterval(timer);
  }
  timer = window.setInterval(() => {
    if (seconds.value > 0) {
      seconds.value--;
    } else {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      emit('countdownEnd');
    }
  }, 1000);
};

onMounted(() => {
  if (props.startCount) {
    startCountdown();
  }
});

onUnmounted(() => {
  if (timer) {
    clearInterval(timer);
  }
});
</script>

<template>
  <span v-if="seconds > 0" class="text-gray-500">{{ seconds }}s</span>
</template>
