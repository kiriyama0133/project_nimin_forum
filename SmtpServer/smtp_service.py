import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtp_service_pb2
import smtp_service_pb2_grpc
import random
import logging
from logging.handlers import RotatingFileHandler
import grpc
from datetime import datetime
from concurrent import futures

# 获取当前日期和时间
current_datetime = datetime.now()

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('Smtp_service.log', maxBytes=2000, backupCount=10)
console_handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
console_handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console_handler)
logger.info("SMTP service started...")

class SmtpService(smtp_service_pb2_grpc.SMTPServicer):
    def SendMail(self, request, context):
        email = request.email
        smtp_server = "smtp.qq.com"
        port = 587  # SMTP port
        sender_email = "kiriyama_0133@qq.com"  # Sender's email
        password = "ddmvnuiwjaykcjjh"  # Sender's email password
        receiver_email = email  # Receiver's email

        try:
            # Validate the email domain
            if '@stu.swpu.edu.cn' in email:
                # Connect to the SMTP server
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls()  # Enable TLS encryption
                    server.login(sender_email, password)  # Login to the server

                    # Create email content
                    subject = '欢迎使用swpu匿名平台！A_A'
                    verification_code = self.generate_verification_code()
                    message = f'您的验证码为: {verification_code}'

                    # Prepare email
                    email_msg = MIMEMultipart()
                    email_msg['From'] = sender_email
                    email_msg['To'] = receiver_email
                    email_msg['Subject'] = subject
                    email_msg.attach(MIMEText(message, 'plain'))

                    # Send the email
                    server.send_message(email_msg)
                    logger.info(f"{current_datetime} - Email sent successfully to: {email}")
                    server.quit()
                    return smtp_service_pb2.SendMailResponse(status="邮件发送成功!" ,message=verification_code)
            else:
                logger.warning(f"{current_datetime} - Invalid or non-whitelisted email: {email}")
                return smtp_service_pb2.SendMailResponse(status="邮箱格式不正确或非白名单邮箱")
        except Exception as e:
            logger.error(f"{current_datetime} - Failed to send email to {email}: {e}")
            return smtp_service_pb2.SendMailResponse(status=f"邮件发送失败: {e}")

    def generate_verification_code(self):
        """Generate an 8-digit verification code."""
        return ''.join([str(random.randint(0, 9)) for _ in range(8)])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smtp_service_pb2_grpc.add_SMTPServicer_to_server(SmtpService(), server)
    server.add_insecure_port('[::]:50052')
    logger.info("Server started on port 50052...")
    server.start()
    server.wait_for_termination()

# Run the server
if __name__ == '__main__':
    serve()
