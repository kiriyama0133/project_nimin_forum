<template>
  <div class="card-container" @click="toggleFlip">
    <div class="card" :class="{ 'is-flipped': isFlipped }">
      <div class="card-front">
        <h2>正面</h2>
        <p>点击翻转卡片</p>
      </div>
      <div class="card-back">
        <h2>背面</h2>
        <p>这是卡片的背面内容</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isFlipped = ref(false)

const toggleFlip = () => {
  isFlipped.value = !isFlipped.value
}
</script>

<style scoped>
.card-container {
  width: 300px;
  height: 400px;
  perspective: 1000px;
  cursor: pointer;
}

.card {
  width: 100%;
  height: 100%;
  position: relative;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.card.is-flipped {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-front {
  background-color: #3498db;
  color: white;
  z-index: 2;
}

.card-back {
  background-color: #2ecc71;
  color: white;
  transform: rotateY(180deg);
}
</style>