export interface AddReplyCardClient {
    number: number;
    id: string; 
    content: string;
    time: string;
    reply?: string; 
    imageUrls?: string[]; // ADDED for reply images
}

export interface ReplyCardRequest {
    number: number;
    skip: number;
}

export interface AddReplyCardResponse {
    message: string;
    data: AddReplyCardClient[];
} 