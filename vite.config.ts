import { defineConfig, loadEnv } from 'vite';
import type { UserConfig } from 'vite';
import path from 'node:path';
import electron from 'vite-plugin-electron/simple';
import vue from '@vitejs/plugin-vue';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig(({ command, mode }): UserConfig => {
  // 加载环境变量，只加载以 VITE_ 开头的变量
  const env = loadEnv(mode, process.cwd(), 'VITE_');
  
  // 打印环境变量（仅在开发环境）
  if (command === 'serve') {
    console.log('API URL:', env.VITE_API_URL);
    console.log('App Title:', env.VITE_APP_TITLE);
  }
  
  return {
    server: {
      port: 15175, // 开发服务器端口
    },
    base: '/', // 设置为你的子路径
    plugins: [
      vue(),
      tailwindcss(),
      electron({
        main: {
          entry: 'electron/main.ts', // 主进程入口文件
        },
        preload: {
          input: path.join(__dirname, 'electron/preload.ts'), // 预加载脚本入口文件
        },
        renderer: process.env.NODE_ENV === 'test' ? undefined : {},
      }),
    ],
    define: {
      'import.meta.env.BASE_URL': JSON.stringify('/'), // 注入默认值
      // 只注入 VITE_ 开头的环境变量
      ...Object.keys(env).reduce((acc, key) => {
        acc[`import.meta.env.${key}`] = JSON.stringify(env[key]);
        return acc;
      }, {} as Record<string, string>)
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'), // 路径别名
      },
    },
    build: {
      outDir: 'dist', // 打包输出目录
      assetsDir: 'assets', // 静态资源输出目录
      rollupOptions: {
        output: {
          assetFileNames: 'assets/[name]-[hash][extname]', // 静态资源文件命名规则
          chunkFileNames: 'assets/[name]-[hash].js', // 代码分块文件命名规则
          entryFileNames: 'assets/[name]-[hash].js', // 入口文件命名规则
        },
      },
    },
  };
});

