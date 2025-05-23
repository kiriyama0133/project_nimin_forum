import { createRouter, createWebHashHistory } from 'vue-router';
import PreferencesView from '../views/PreferencesView.vue'
const baseUrl = (import.meta.env && import.meta.env.BASE_URL) || '/';
const router = createRouter({
  history: createWebHashHistory(baseUrl), // 使用 hash 模式
  routes: [
    {
      path: '/',
      name: '默认路径',
      redirect: '/loginview',
    },
    {
      path: '/login',
      name: '登录',
      component: () => import('../components/FormContaniers/login.vue'),
    },
    {
      path: '/register',
      name: '注册',
      component: () => import('../components/FormContaniers/register.vue'),
    },
    {
    path: '/favoritepage',
      name: '收藏界面',
      component: () => import('../views/favoritepage.vue'),
      children: [
        {
          path: '/favorite',
          name: '收藏',
          component: () => import('../views/pages/favorite.vue'), 
        },
      ]
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
          path: '/create',
          name: '创作',
          component: () => import('../views/pages/create.vue'),
        },
        {
          path: '/game',
          name: '游戏',
          component: () => import('../views/pages/game.vue'),
        },
        {
          path: '/life',
          name: '生活',
          component: () => import('../views/pages/life.vue'),
        },
        {
          path: '/settings',
          name: '设置',
          component: () => import('../views/settings.vue'), 
        },
        {
          path: '/cookies',
          name: '饼干',
          component: () => import('../views/cookies.vue'), 
        },
        {
          path: '/preferences',
          name: '偏好设置',
          component: PreferencesView
        },
        {
          path: '/mycard',
          name: '我的帖子',
          component: () => import('../views/MyreplyPage.vue'),
        },
        {
          path: '/search',
          name: '搜索',
          component: () => import('../views/SearchPage.vue'),
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
