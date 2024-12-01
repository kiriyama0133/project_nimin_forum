using System;
using System.Threading.Tasks;
using Grpc.Core;  // 引入 Grpc.Core 命名空间
using Cookie;  // 引入通过 proto 文件生成的命名空间

class Program
{
    static async Task Main(string[] args)
    {
        // 使用 Grpc.Core 创建 gRPC 客户端，连接到服务器
        var channel = new Channel("localhost:50051", ChannelCredentials.Insecure);

        // 创建 CookieService 客户端
        var client = new CookieService.CookieServiceClient(channel);

        // 调用 AddCookie 方法作为示例
        var addCookieRequest = new CookieRequest_Add
        {
            Email = "test@example.com"
        };

        var addCookieResponse = await client.AddCookieAsync(addCookieRequest);

        Console.WriteLine("AddCookie Response: " + addCookieResponse.Status + " - " + addCookieResponse.Message);

        // 获取 Cookie 信息
        var getCookieRequest = new CookieRequest_ByID { Id = 1 };
        var getCookieResponse = await client.GetCookieByIDAsync(getCookieRequest);

        Console.WriteLine("GetCookieByID Response: Name - " + getCookieResponse.Name + ", Email - " + getCookieResponse.Email);

        // 关闭连接
        await channel.ShutdownAsync();
    }
}
