import axios, { InternalAxiosRequestConfig } from 'axios';

// 创建axios实例
const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL,  // 确保这里只有基础URL，不包含 /api/v1
  timeout: 30000,  // 增加超时时间，因为上传可能需要更长时间
  headers: {
      'Accept': 'application/json',
  },
});

// 请求拦截器
axiosInstance.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
      // 如果是上传请求，不设置 Content-Type，让浏览器自动设置
      if (config.data instanceof FormData) {
          delete config.headers['Content-Type'];
      }

      // 添加Token
      const token = localStorage.getItem('access_token');
      if (token) {
          config.headers['Authorization'] = `Bearer ${token}`;
      }

      // 打印请求信息
      // console.log('=== 请求信息 ===');
      // console.log('完整URL:', `${config.baseURL}${config.url}`);
      // console.log('方法:', config.method);
      // console.log('请求头:', config.headers);
      
      if (config.data instanceof FormData) {
          console.log('FormData内容:');
          for (let pair of config.data.entries()) {
              console.log(pair[0] + ': ' + (pair[1] instanceof File ? 
                  `File(${pair[1].name}, ${pair[1].type}, ${pair[1].size}bytes)` : 
                  pair[1]));
          }
      }

      return config;
  },
  (error) => {
      console.error('请求拦截器错误:', error);
      return Promise.reject(error);
  }
);

// 响应拦截器
axiosInstance.interceptors.response.use(
    (response) => {
      // console.log('=== 响应成功 ===');
      // console.log('响应状态:', response.status);
      // console.log('响应头:', response.headers);
      // console.log('响应数据:', response.data);
      return response;
    },
    (error) => {
      console.error('=== 响应错误 ===');
      console.error('错误配置:', error.config);
      console.error('错误状态:', error.response?.status);
      console.error('错误数据:', error.response?.data);
      
      if (error.response) {
        switch (error.response.status) {
          case 401:
            console.error('认证失败，请检查token是否有效');
            throw new Error('认证失败，请重新登录');
          case 413:
            console.error('文件大小超出限制');
            throw new Error('图片文件太大');
          case 415:
            console.error('不支持的媒体类型');
            throw new Error('不支持的图片格式');
          case 404:
            console.error('请求的接口不存在，完整URL:', error.config?.baseURL + error.config?.url);
            throw new Error(`请求的接口不存在: ${error.config?.baseURL}${error.config?.url}`);
          default:
            console.error('服务器错误:', error.response.data);
            throw new Error(error.response.data?.message || '图片上传失败');
        }
      } else if (error.request) {
        console.error('未收到响应:', error.request);
        throw new Error('网络请求失败，请检查网络连接');
      } else {
        console.error('请求配置错误:', error.message);
        throw new Error('图片上传失败：' + error.message);
      }
    }
);



// // 在 uploadImages 函数之前添加测试函数
// export async function testUploadRoute(): Promise<void> {
//   try {
//     // console.log('=== 测试上传路由 ===');
//     const response = await axiosInstance.get('/api/v1/upload/test');
//     console.log('测试路由响应:', response.data);
//   } catch (error: any) {
//     // console.error('测试路由失败:', error);
//     throw error;
//   }
// }

// 修改 uploadImages 函数
export async function uploadImages(files: File[]): Promise<string[]> {
  console.log('=== 开始上传图片 ===');
  console.log('文件数量:', files.length);
  
  try {
    // 先测试路由是否可用
    // await testUploadRoute();
    
    // 打印文件信息
    files.forEach((file, index) => {
      console.log(`文件 ${index + 1}:`, {
        name: file.name,
        type: file.type,
        size: file.size,
        lastModified: file.lastModified
      });
    });

    const formData = new FormData();
    files.forEach(file => {
      formData.append('imageFiles', file);
      // console.log('已添加文件到FormData:', file.name);
    });

    // 使用完整的API路径
    const apiPath = '/api/v1/upload/upload-image';
    // console.log('准备发送请求到:', apiPath);
    // console.log('完整请求URL:', import.meta.env.VITE_API_URL + apiPath);
    
    const response = await axiosInstance.post(apiPath, formData);
    
    // console.log('上传成功，响应数据:', response.data);

    if (!response.data?.data || !Array.isArray(response.data.data)) {
      console.error('响应数据格式不正确:', response.data);
      throw new Error('服务器返回的图片URL格式不正确');
    }

    // console.log('上传完成，返回的URL列表:', response.data.data);
    return response.data.data;
  } catch (error: any) {
    console.error('图片上传过程出错:', error);
    throw error;
  }
}

// 导出axios实例
export default axiosInstance;