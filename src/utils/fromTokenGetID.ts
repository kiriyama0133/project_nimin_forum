import { jwtDecode } from "jwt-decode";

// 定义 Token Payload 的基本结构 (可以根据实际情况扩展)
interface DecodedTokenPayload {
  sub?: string; // 'sub' 声明通常包含用户 ID
  exp?: number; // 过期时间 (可选)
  // 可能还有其他自定义声明，例如：
  // user_id?: string;
  // username?: string;
}

/**
 * 从 localStorage 获取 Access Token 并解码以提取用户 ID。
 * @returns {string | null} 返回用户 ID (通常是 'sub' 声明)，如果 Token 不存在、无效或没有 'sub' 声明，则返回 null。
 */

export const getUserIdFromToken = (): string | null => {
  const token = localStorage.getItem('access_token');

  if (!token) {
    console.warn("无法获取用户 ID，因为 localStorage 中没有 access_token。");
    return null;
  }

  try {
    // 解码 Token Payload
    const decodedPayload = jwtDecode<DecodedTokenPayload>(token);

    // 检查 Token 是否过期 (可选但推荐)
    if (decodedPayload.exp && Date.now() >= decodedPayload.exp * 1000) {
        console.warn("Token 已过期。");
        localStorage.removeItem('access_token'); // 移除过期的 token
        return null;
    }

    // 提取 'sub' 声明作为用户 ID
    if (decodedPayload.sub) {
      console.log("从 Token 解码出的用户 ID (sub):", decodedPayload.sub); // 可以取消注释用于调试
      return decodedPayload.sub;
    } else {
      console.warn("在解码的 Token Payload 中未找到 'sub' 声明。");
      return null;
    }

  } catch (error) {
    console.error("解码 Token 时出错:", error);
    // 如果解码失败，可能是 Token 格式错误，移除它
    localStorage.removeItem('access_token');
    return null;
  }
};