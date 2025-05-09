import axios from 'axios';
const axiosComfirm = 
axios.create({
    baseURL: 'https://localhost/api/v1', // 后端服务的基础 URL
    timeout: 5000, // 请求超时时间（毫秒）
    headers: {
      'Content-Type': 'application/json', // 默认请求头
    },
  });
  axiosComfirm.interceptors.request.use(
    (config) => {
      //在发送请求之前可以添加额外的逻辑，比如添加认证 token
      console.log('Request:', config);
      return config;
    },
    (error) => {
      //请求错误处理
      console.error('Request Error:', error);
      return Promise.reject(error);
    }
  );
  
  //响应拦截器
  axiosComfirm.interceptors.response.use(
    (response) => {
      //对响应数据进行处理
      console.log('Response:', response);
      return response; // 直接返回响应数据
    },
    (error) => {
      //响应错误处理
      console.error('Response Error:', error);
      return Promise.reject(error);
    }
  );
  
  //导出封装的 Axios 实例
  export default axiosComfirm;