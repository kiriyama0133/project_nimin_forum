<script setup lang="ts">
import svg from '../assets/bg/icons8.gif'
import routecard from './routecard.vue';
// Define the structure for card items
interface CardItem {
  id: number;
  type: 'text' | 'image'| 'component';
  title?: string;
  description?: string;
  imageSrc?: string;
  link?: string;
  slotContent?: {
    header?: string | import('vue').Component;
    head?: string | import('vue').Component;
    content?: string | import('vue').Component;
  }
  component?: import('vue').Component; // 新增自定义组件支持
}

// Props for the component
interface Props {
  cards?: CardItem[];
  rotateSpeed?: number;
  count?: number;
}

// Default props values
const props = withDefaults(defineProps<Props>(), {
  cards: () => [
    {
      id: 1,
      type: 'text',
      title: '3/29',
      imageSrc: svg,
      description: '😄差不多得了',
      link: ''
    },
    {
      id: 2,
      type: 'text',
      title: '3/28',
      description: '+1',
      link: ''
    },
    {
      id: 3,
      type: 'text',
      title: '2020-2024',
      description: 'Model for generating highly dimensional, mostly numeric, tabular data',
      link: ''
    },
    {
      id: 4,
      type: 'component',
      component:routecard,
    },
    {
      id: 5,
      type: 'text',
      title: '2024-2025',
      description: '新年快乐！♥',
      link: ''
    },
    {
      id: 6,
      type: 'component',
      component:routecard,
      slotContent: {
        head: '一条新的回复',
        content: '对的！对的！',
      },
    },
  ],
  rotateSpeed: 40,
  count: 8
});
</script>

<template>
  <div class="void overflow: hidden; " id="void" :style="`--rotate-speed: ${rotateSpeed}; --count: ${count};`">
    <div class="crop overflow: hidden;">
      <ul class="card-list" :style="`--count:${props.cards.length};`">
        <li v-for="(card, index) in props.cards" :key="card.id" :style="`animation-delay: calc((var(--rotate-speed)/var(--count)) * -${index}s);`">
          <div class="card" :style="`animation-delay: calc((var(--rotate-speed)/var(--count)) * -${index}s);`">         
              <template v-if="card.type === 'text'">
                <span>{{ card.title }}</span>
                <span>{{ card.description }}</span>
              </template>
              <template v-else-if="card.type === 'image'">
                <img :src="card.imageSrc" alt="">
              </template>
              <template v-if="card.type === 'component'">
        <component :is="card.component">
          <!-- 默认插槽 -->
          <template v-slot:header>
            <div v-if="typeof card.slotContent?.header === 'string'">
              {{ card.slotContent.header }}
            </div>
            <component 
              v-else-if="card.slotContent?.header" 
              :is="card.slotContent.header" 
            />
          </template>

          <!-- 头部插槽 -->
          <template v-slot:head>
            <div v-if="typeof card.slotContent?.head === 'string'">
              {{ card.slotContent.head }}
            </div>
            <component 
              v-else-if="card.slotContent?.head" 
              :is="card.slotContent.head" 
            />
          </template>
                    <!-- 内容插槽 -->
                    <template v-slot:content>
            <div v-if="typeof card.slotContent?.content === 'string'">
              {{ card.slotContent.content }}
            </div>
            <component 
              v-else-if="card.slotContent?.content" 
              :is="card.slotContent.content" 
            />
          </template>
        </component>
      </template>
          </div>
        </li>
      </ul>
      <div class="last-circle" />
      <div class="second-circle" />
    </div>
    <div class="mask" />
    <div class="center-circle bg-[url('src/assets/bg/200h.gif')] bg-cover" />
  </div>
</template>

<style scoped>
/* Define CSS variables at component level */
.void {
  --rotate-speed: v-bind('rotateSpeed');
  --count: v-bind('count');
  --easing: cubic-bezier(0.000, 0.37, 1.000, 0.63);
}

/* Container styles */
.void {
  width: 100%;
  max-width: 1024px;
  margin: auto;
  position: relative;
  aspect-ratio: 1 / 1;
}

/* Pause animation on hover */
/* ul:hover * {
  animation-play-state: paused;
} */

/* List styles */
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  position: relative;
  width: 100%;
  aspect-ratio: 1 / 1;
  z-index: 1;
}

/* List item styles */
li {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
  animation: rotateCW calc(var(--rotate-speed) * 1s) var(--easing) infinite;
}
/* Card styles */
.card {
  width: 27%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 16px 24px;
  gap: 8px;
  background: #FFFFFF;
  box-shadow: 0px 4px 12px rgba(70, 0, 255, 0.1), 0px 16px 32px rgba(165, 135, 255, 0.1);
  border-radius: 12px;
  font: 400 14px '';
  color: #535062;
  animation: rotateCCW calc(var(--rotate-speed) * 1s) var(--easing) infinite;
}

/* Image styles */
.card img {
  width: 100%;
}

/* Link styles */
a {
  text-decoration: none;
  color: unset;
  display: block;
  height: 80px;
  overflow: hidden;
}

/* Model name styles */
.model-name {
  font-weight: 500;
  font-size: 18px;
  line-height: 150%;
  color: #3B2ED0;
  display: block;
}

/* SVG styles */
svg {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
}

/* Define clockwise rotation animation */
@keyframes rotateCW {
  from {
    transform: translate3d(-100px, -200%, 0) rotate(-5deg); /* 减小半径 */
  }
  to {
    transform: translate3d(-100px, -200%, 0px) rotate(-315deg); /* 减小半径 */
  }
}
/* Define counter-clockwise rotation animation */
@keyframes rotateCCW {
  from {
    transform: translate3d(0px, -30%, 0px) rotate(5deg); /* 减小半径 */
  }
  to {
    transform: translate3d(0px, -30%, 0px) rotate(315deg); /* 减小半径 */
  }
}
/* Center circle styles */
.center-circle {
  position: absolute;
  width: 200px;
  aspect-ratio: 1 / 1;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  
  box-shadow: 0px 18px 36px -18px rgba(12, 5, 46, 0.3),
    0px 30px 60px -12px rgba(12, 5, 46, 0.25);
  border-radius: 50%;
  background-size: cover;
  background-position: -35px 0;
  overflow: hidden;
}

/* Second circle styles */
.second-circle {
  position: absolute;
  width: 30%;
  aspect-ratio: 1 / 1;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background: #F5F4FE;
  opacity: 0.5;
  box-shadow: 0px 18px 36px -18px rgba(12, 5, 46, 0.3),
    0px 30px 60px -12px rgba(12, 5, 46, 0.25);
  border-radius: 50%;
  background-image: url(../assets/bg/03.gif);
  overflow: hidden;
}

/* Last circle styles */
.last-circle {
  position: absolute;
  width: 44%;
  aspect-ratio: 1 / 1;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background: #F5F4FE;
  opacity: 0.25;
  box-shadow: 0px 18px 36px -18px rgba(12, 5, 46, 0.3), 0px 30px 60px -12px rgba(12, 5, 46, 0.25);
  border-radius: 50%;
  background-image: url(../assets/bg/03.gif);
  overflow: hidden;
}

/* Crop styles */
.crop {
  mask-image: linear-gradient(90deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0) 50%);
  -webkit-mask-image: linear-gradient(90deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0) 50%,
    rgba(0, 0, 0, 1) 50%, rgba(0, 0, 0, 1));
}

/* Mask styles */
.mask {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 50%;
  background-position: 100% 50%;
  background-repeat: no-repeat;
  background-image: radial-gradient(100% 50% at 100% 50%, rgba(60, 26, 229, 0.25) 0%,
    rgba(59, 26, 229, 0.241896) 20%,
    rgba(53, 26, 229, 0.1872) 40%,
    rgba(41, 23, 240, 0.104) 60%,
    rgba(34, 26, 229, 0.0184296) 90%, rgba(32, 26, 229, 0) 100%);
}

/* Mask after effect */
.mask:after {
  content: "";
  position: absolute;
  width: 1px;
  height: 100%;
  right: 0;
  display: block;
  background-image: linear-gradient(180deg, rgba(60, 26, 229, 0) 0%, #3C1AE5 50%, rgba(60, 26, 229, 0) 100%);
}
</style>
