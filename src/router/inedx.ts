import { createRouter, createWebHistory } from 'vue-router';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // 使用 history 模式
  routes: [
    {
      path: '/',
      name: '默认路径',
      redirect: '/loginview',
    },
    {
      path: '/login',
      name: '登录',
      component: () => import('../views/login.vue'),
    },
    {
      path: '/register',
      name: '注册',
      component: () => import('../views/register.vue'),
    },
    {
      path: '/homepage',
      name: '主界面',
      component: () => import('../views/homepage.vue'),
      children: [
        {
          path: '/Introduction',
          name: '介绍',
          component: () => import('../views/Introduction.vue'),
        },
        {
          path: '/contentpage',
          name: '内容页',
          component: () => import('../views/contentpage.vue'),
        },
        {
          path: '/time',
          name: '时间',
          component: () => import('../views/pages/time.vue'),
        },
        {
          path: '/total',
          name: '综合',
          component: () => import('../views/pages/total.vue'),
        },
        {
          path: '/subculture',
          name: '亚文化',
          component: () => import('../views/pages/subculture.vue'),
        },
        {
          path: '/settings',
          name: '设置',
          component: () => import('../views/settings.vue'), 
        },
        {
          path: '/favorate',
          name: '收藏',
          component: () => import('../views/favorate.vue'), 
        },
        {
          path: '/cookies',
          name: '饼干',
          component: () => import('../views/cookies.vue'), 
        },

      ]
    },
    {
      path: '/loginview',
      name: '主页',
      component: () => import('../views/loginview.vue'),
    },
    
  ],
});
export default router;
