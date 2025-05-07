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
  
  //响应拦截器
  axiosInstance.interceptors.response.use(
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
  export default axiosInstance;

export interface CookieApiResponse {
  message: string;
}

export const addCookie = async (): Promise<CookieApiResponse> => {
  try {
    // The backend is expected to always return a JSON object with a 'message' field,
    // even for logical errors like "cookies不足", with a 200 OK status.
    const response = await axiosInstance.get<CookieApiResponse>('/addcookie');
    return response.data;
  } catch (error: any) {
    console.error('Error calling /addcookie API:', error);

    // This catch block handles network errors or unexpected server errors
    // (e.g., 500, or 4xx if not handled by the backend to return a Message object).
    if (error.response && error.response.data && typeof error.response.data.message === 'string') {
      // If the server did return an error response with a 'message' field (e.g. some specific error middleware)
      return { message: error.response.data.message };
    } else if (error.response && error.response.data && typeof error.response.data.detail === 'string') {
      // FastAPI validation errors often use 'detail'
      return { message: error.response.data.detail };
    } else if (error.request) {
      // The request was made but no response was received
      return { message: '无法连接到服务器，请检查您的网络连接并稍后再试。' };
    } else {
      // Something else happened in setting up the request that triggered an Error
      return { message: '添加Cookie时发生未知错误，请稍后再试。' };
    }
  }
};
