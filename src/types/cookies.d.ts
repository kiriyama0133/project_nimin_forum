export interface Cookie{
    name: string;
    time: string;
    isbanned: boolean;
    inused: boolean;
    id: string;
}

export interface CookieResponse{
    data: Cookie[];
}

export interface UserCookieNumberResponse{
    number: number;
}
