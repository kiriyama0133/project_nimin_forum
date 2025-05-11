import { defineConfig } from 'vite';
import path from 'node:path';
import electron from 'vite-plugin-electron/simple';
import vue from '@vitejs/plugin-vue';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  server: {
    port: 5174, // 开发服务器端口
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
});
