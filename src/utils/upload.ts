import axios from 'axios';
const axiosInstance = 
axios.create({
    baseURL: import.meta.env.VITE_API_URL + '/api/v1/upload', // 后端服务的基础 URL
    timeout: 5000, // 请求超时时间（毫秒）
    headers: {
      'Content-Type': 'multipart/form-data', // 默认请求头
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


      return config;
    },
    (error) => {
      //请求错误处理
      console.error('Request Error:', error);
      return Promise.reject(error);
    }
  );
  
  //响应拦截器
  axiosInstance.interceptors.response.use(
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
  export default axiosInstance;
export async function getOneCard(number:number): Promise<any> {
  try {
    const response = await axiosInstance.get(`getonecard/${number}`);
    return response.data;
  } catch (error: any) {
    console.error('Error fetching card:', error);
    return null; // Return null in case of error
  }
}
