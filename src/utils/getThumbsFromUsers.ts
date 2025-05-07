import axios from 'axios'

const getthumbs = axios.create({
  baseURL: 'https://localhost:8000/api/v1/cards', // 注意这里改成 /cards，无需 v1
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
})
 //请求拦截器
 getthumbs.interceptors.request.use(
    (config) => {
      // --- 添加 Token 到请求头 ---
      // 1. 从 localStorage 获取 token
      const token = localStorage.getItem('access_token');
      
      // 2. 如果 token 存在，添加到 Authorization 请求头
      if (token) {
        // 确保 headers 对象存在
        config.headers = config.headers || {};
        // 添加 Bearer Token
        config.headers['Authorization'] = `Bearer ${token}`;
        console.log("getthumbs: Adding Authorization header");
      } else {
        console.log("getthumbs: No token found, request sent without Authorization header");
      }
      // ------------------------
      
      // console.log('Original Request Config:', config); // 可以保留或移除原始日志
      return config;
    },
    (error) => {
      //请求错误处理
      console.error('Request Error:', error);
      return Promise.reject(error);
    }
  );
  getthumbs.interceptors.response.use(
    (response) => {
      //对响应数据进行处理
      console.log('Response:', response);
      // console.log('获取到的卡片数据：', response.data); //json数据集
      // console.log('获取到的里层数据：', response.data.data); //列表
      return response; // 直接返回响应数据
    },
    (error) => {
      //响应错误处理
      console.error('Response Error:', error);
      return Promise.reject(error);
    }
  );
  
  //导出封装的 Axios 实例
  export default getthumbs;
