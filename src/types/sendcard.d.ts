export interface AddReplyCardClient{
    number: number;
    id: string; // ID of the user sending the reply
    content: string;
    time: string;
    reply?: string; // ID of the user being replied to (optional)
}
// --- Interfaces for fetching replies ---
export interface AddReplyCard { // Structure of a single reply card received from backend
    number: number; // Original post number it belongs to
    id: string; // User ID of the replier
    content: string;
    time: string;
    imageUrls: string[];
    reply?: string; // User ID being replied to, if any
    thumbs?: number;
    number_primary:string; // Optional, based on sendcard component props
    // Add any other fields that AddReplyCard from your backend has and sendcard component uses
}
export interface ReplyCardRequest {
number: number; // The number of the original post to fetch replies for
skip?: number;
}

export interface AddReplyCardResponse {
data: AddReplyCard[];
}

// Assuming DefaultCard structure based on typical usage and backend model hints
export interface DefaultCard {
    id: string; 
    content: string;
    time: string;
    number: number; 
    category: string;
    imageUrls: string[];
  }
  
  export interface NewCardRequest {
    category: string;
  }
  
  export interface NewCardResponse {
    data: DefaultCard | null;
  }

// 用户查看自己发表的帖子
export interface UserCardRequest {
    Cookie: string | null;
    skip: number;
}

// 用户查看自己发表的帖子响应
export interface UserCardResponse {
    DefaultCard: DefaultCard[];
    AddReplyCard: AddReplyCard[];
}
// --- End Interfaces for fetching replies ---
