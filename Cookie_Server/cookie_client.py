import grpc
import cookie_service_pb2
import cookie_service_pb2_grpc

# 调试日志：捕获并打印异常
def run():
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = cookie_service_pb2_grpc.CookieServiceStub(channel)

            # 调用 AddCookie 服务
            print("Sending AddCookie request...")
            response = stub.AddCookie(cookie_service_pb2.CookieRequest_Add(email="test@example.com"))
            print("AddCookie response:", response.message)

            # 调用 QueryCookie 服务
            print("Sending QueryCookie request...")
            response = stub.QueryCookie(cookie_service_pb2.CookieRequest_Query(name="XOjkqaG"))
            print("QueryCookie response:", response.message)

            # 调用 GetCookieByID 服务
            print("Sending GetCookieByID request...")
            response = stub.GetCookieByID(cookie_service_pb2.CookieRequest_ByID(id=1))
            print("GetCookieByID response:", response.name, response.email)

            # 调用 GetCookieByName 服务
            print("Sending GetCookieByName request...")
            response = stub.GetCookieByName(cookie_service_pb2.CookieRequest_ByName(name="XOjkqaG"))
            print("GetCookieByName response:", response.id, response.email)

            # 调用 GetCookiesByEmail 服务
            print("Sending GetCookiesByEmail request...")
            response = stub.GetCookiesByEmail(cookie_service_pb2.CookieRequest_ByEmail(email="test@example.com"))
            for cookie in response.cookies:
                print(f"Cookie Name: {cookie.name}, ID: {cookie.id}")

    except grpc.RpcError as e:
        # 捕获并打印 gRPC 错误
        print(f"gRPC error occurred: {e.code()}: {e.details()}")
        print("Debug Info:", e.debug_error_string())
    except Exception as e:
        # 捕获并打印其他错误
        print(f"An error occurred: {e}")
        print("Debug Info:", str(e))

if __name__ == '__main__':
    run()
