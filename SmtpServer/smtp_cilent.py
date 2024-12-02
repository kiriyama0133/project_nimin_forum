import grpc
import smtp_service_pb2
import smtp_service_pb2_grpc

def send_email():
    # Create gRPC channel and stub
    channel = grpc.insecure_channel('localhost:50052')
    stub = smtp_service_pb2_grpc.SMTPStub(channel)
    
    # Create request object
    request = smtp_service_pb2.SendMailRequest(email="202331094154@stu.swpu.edu.cn")
    
    # Call the SendMail method
    response = stub.send_email(request)
    
    # Print the response
    print(f"Response: {response.status}")

if __name__ == "__main__":
    send_email()
