import axios from 'axios';
import type { CookieResponse, UserCookieNumberResponse } from '../types/cookies';

const axiosInstance = 
axios.create({
    baseURL: import.meta.env.VITE_API_URL + '/api/v1/cookies', // 后端服务的基础 URL
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
        // console.log("axiosInstance: Adding Authorization header");
      } else {
        // console.log("axiosInstance: No token found, request sent without Authorization header");
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
      // console.log('Response:', response);
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

// --- Shared Interface for API responses that return a simple message ---
export interface CookieApiResponse {
  message: string;
}

// --- Function to add a new cookie ---
export const addCookie = async (): Promise<CookieApiResponse> => {
  try {
    const response = await axiosInstance.get<CookieApiResponse>('addcookie');
    return response.data; 
  } catch (error: any) {
    console.error('Error calling /api/v1/cookies/addcookie API:', error);
    if (error.response && error.response.data && typeof error.response.data.message === 'string') {
      return { message: error.response.data.message };
    } else if (error.response && error.response.data && typeof error.response.data.detail === 'string') {
      return { message: error.response.data.detail };
    } else if (error.request) {
      return { message: '无法连接到服务器，请检查您的网络连接并稍后再试。' };
    } else {
      return { message: '添加Cookie时发生未知错误，请稍后再试。' };
    }
  }
};

// --- Function to fetch user cookies ---
// Uses CookieResponse from ../types/cookies.ts
export const fetchUserCookies = async (): Promise<CookieResponse> => {
  try {
    const response = await axiosInstance.get<CookieResponse>('getcookie');
    return response.data;
  } catch (error: any) {
    console.error('Error calling /api/v1/cookies/getcookie API:', error);
    if (error.response && error.response.data) {
      throw new Error(error.response.data.detail || error.response.data.message || '获取Cookie列表失败');
    } else if (error.request) {
      throw new Error('无法连接到服务器，获取Cookie列表失败。');
    }
    throw new Error('获取Cookie列表时发生未知错误。');
  }
};

// --- Interface for the /use_cookie payload ---
export interface UseCookiePayload {
  name: string;
}

// --- Function to set a cookie as active on the backend ---
// Returns CookieApiResponse
export const setActiveBackendCookie = async (cookieName: string): Promise<CookieApiResponse> => {
  try {
    const payload: UseCookiePayload = { name: cookieName };
    // POST request to /api/v1/cookies/use_cookie
    const response = await axiosInstance.post<CookieApiResponse>('use_cookie', payload);
    return response.data; // Expects a Message object { message: string }
  } catch (error: any) {
    console.error('Error calling /api/v1/cookies/use_cookie API:', error);
    if (error.response && error.response.data && typeof error.response.data.message === 'string') {
      return { message: error.response.data.message };
    } else if (error.response && error.response.data && typeof error.response.data.detail === 'string') {
      return { message: error.response.data.detail };
    } else if (error.request) {
      return { message: '无法连接到服务器，启用Cookie失败。' };
    }
    return { message: '启用Cookie时发生未知错误。' };
  }
};

// 获取用户的获取cookie的剩余次数
export const getUserCookieNumber = async (): Promise<UserCookieNumberResponse> => {
    try {
        const response = await axiosInstance.get<UserCookieNumberResponse>('getusercookienum');
        return response.data;
    } catch (error: any) {
        console.error('Error calling /api/v1/cookies/getusercookienum API:', error);
        throw new Error('获取用户获取cookie的剩余次数失败。');
    }
}
