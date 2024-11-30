import grpc
import cookie_service_pb2
import cookie_service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = cookie_service_pb2_grpc.CookieServiceStub(channel)
        
        # 调用 AddCookie 服务
        response = stub.AddCookie(cookie_service_pb2.CookieRequest_Add(email="test@example.com"))
        print("AddCookie response:", response.message)

        # 调用 QueryCookie 服务
        response = stub.QueryCookie(cookie_service_pb2.CookieRequest_Query(name="XOjkqaG"))
        print("QueryCookie response:", response.message)

        #调用TestCookie服务
        response = stub.TestCookie(cookie_service_pb2.CookieRequest_Test())
        print("TestCookie response:", response.message)

if __name__ == '__main__':
    run()
