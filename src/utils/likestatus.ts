import axios from 'axios';
const axiosInstance = 
axios.create({
    baseURL: 'http://localhost:8000/api/v1/cards', // 后端服务的基础 URL
    timeout: 5000, // 请求超时时间（毫秒）
    headers: {
      'Content-Type': 'application/json', // 默认请求头
    },
  });
  
  //请求拦截器
  axiosInstance.interceptors.request.use(
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
        console.log("axiosInstance: Adding Authorization header");
      } else {
        console.log("axiosInstance: No token found, request sent without Authorization header");
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
  export default axiosInstance;