export interface AddReplyCardClient {
    number: number;
    id: string; 
    content: string;
    time: string;
    reply?: string; 
    imageUrls?: string[]; // ADDED for reply images
}

export interface sendcarddata {
    number: number;
    id: string; 
    content: string;
    time: string;
    reply?: string; 
    imageUrls?: string[]; // ADDED for reply images
    thumbs: number;
    number_primary: string;
}

export interface ReplyCardRequest {
    number: number;
    skip: number;
}

export interface AddReplyCardResponse {
    message: string;
    data: sendcarddata[];
} 