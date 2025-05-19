import axios from 'axios'
const axiosInstance = axios.create({
    baseURL: import.meta.env.VITE_API_URL + '/api/v1/cards',  
    timeout: 5000,
    headers: {
      'Content-Type': 'application/json',
    },
  })
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
interface LikeParams {
    reply_id: string
    action: 'like' | 'unlike'
}
export async function toggleLike(params: LikeParams): Promise<void> {
    await axiosInstance.post('/like', params)
  }