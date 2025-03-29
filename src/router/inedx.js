import { createRouter, createWebHistory } from 'vue-router';
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL), // 使用 history 模式
    routes: [
        {
            path: '/',
            name: '默认路径',
            redirect: '/login',
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
            path: '/home',
            name: '主页',
            component: () => import('../views/home.vue'),
        },
    ],
});
export default router;
