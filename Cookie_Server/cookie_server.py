from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker,declarative_base
from sqlalchemy import Column, Text, Integer,String, VARCHAR, TIMESTAMP, BOOLEAN, Float, text
from sqlalchemy.exc import SQLAlchemyError
import random
import string
import logging
import grpc
import cookie_service_pb2
import cookie_service_pb2_grpc
from logging.handlers import RotatingFileHandler
from sqlalchemy.exc import OperationalError
from datetime import datetime
from concurrent import futures
from grpc_reflection.v1alpha import reflection
import time
# 获取当前日期和时间
current_datetime = datetime.now()

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Create a file handler
handler = RotatingFileHandler('Cookie_db.log', maxBytes=2000, backupCount=10)
console_handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
console_handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(console_handler)
logger.info("Starting...")

Base = declarative_base()
class Cookie(Base):
    __tablename__ = 'cookies' #指定类映射到的表名
    __table_args__ = {'comment': 'cookies表'} #添加表注释

    #定义表的列段
    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    name = Column(String(7), nullable=False, comment='name')
    used = Column(BOOLEAN, default=False, comment='used')
    email = Column(String(50), nullable=False, comment='email')

# # 创建数据库引擎（SQLite 示例）
# engine = create_engine('sqlite:///cookies.db')
# # 创建表
# Base.metadata.create_all(engine)

#数据库连接配置
DATABASE_URL = "sqlite:///cookies.db"
engine = create_engine(DATABASE_URL, echo=True)

#创建数据库会话
Session=sessionmaker(bind=engine)
session=Session()

class CookieService(cookie_service_pb2_grpc.CookieServiceServicer):
    def AddCookie(self, request, context):
        try:
            # 生成 Cookie 并保存到数据库
            new_cookie = Cookie(name=self.generate_random_string(), email=request.email, used=False)
            session.add(new_cookie)
            session.commit()
            logger.info(str(current_datetime) + " " + new_cookie.name + " " + "Cookie added successfully.")
            return cookie_service_pb2.CookieResponse(status="success", message="Cookie added successfully.")
        except SQLAlchemyError as e:
            logger.warning(f"添加 Cookie 时出错: {str(e)}")
            session.rollback()
            return cookie_service_pb2.CookieResponse(status="error", message=str(e))

    def generate_random_string(self, length=7):
        """生成一个包含大小写字母的随机字符串"""
        letters = string.ascii_letters  # 包含所有大小写字母
        random_string = ''.join(random.choice(letters) for _ in range(length))
    
        # 如果随机字符串已经存在，则重新生成
        if self.query_cookie(random_string) == "yes":
            self.generate_random_string()  # 递归调用生成新的随机字符串
        return random_string


    def DeleteCookie(self, request, context):
        try:
            # 删除 Cookie
            cookie_to_delete = session.query(Cookie).filter(Cookie.name == request.name).first()
            if cookie_to_delete:
                session.delete(cookie_to_delete)
                session.commit()
                logger.info(str(current_datetime) + " " + request.name + " " + "Cookie deleted successfully.")
                return cookie_service_pb2.CookieResponse(status="success", message="Cookie deleted successfully.")
            else:
                logger.info(str(current_datetime) + " " + request.name + " " + "Cookie not found.")
                return cookie_service_pb2.CookieResponse(status="error", message="Cookie not found.")
        except SQLAlchemyError as e:
            logger.warning(f"删除 Cookie 时出错: {str(e)}")
            session.rollback()
            return cookie_service_pb2.CookieResponse(status="error", message=str(e))
    
    def QueryCookie(self, request, context):
        try:
            # 查询 Cookie
            cookie = session.query(Cookie).filter(Cookie.name == request.name).first()
            if cookie:
                logger.info(str(current_datetime) + " " + request.name + " " + "Cookie found.")
                return cookie_service_pb2.CookieResponse(status="success", message="Cookie found.")
            else:
                logger.info(str(current_datetime) + " " + request.name + " " + "Cookie not found.")
                return cookie_service_pb2.CookieResponse(status="error", message="Cookie not found.")
        except SQLAlchemyError as e:
            logger.warning(f"查询 Cookie 时出错: {str(e)}")
            return cookie_service_pb2.CookieResponse(status="error", message=str(e))
        
    # 定义查询函数
    def query_cookie(self, _name):  # 添加self参数
        try:
            cookies = session.query(Cookie).filter(Cookie.name == _name).first()
            if cookies:  # 如果有记录，返回 True
                logger.info(str(current_datetime) + " " + _name + " " + "Cookie found.")
                return "yes"
            else:  # 没有记录，返回 False
                logger.info(str(current_datetime) + " " + _name + " " + "Cookie not found.")
                return "false"
        except SQLAlchemyError as e:
            logger.warning(f"查询出错: {str(e)}")
            return "false"
        
    def TestCookie(self, request, context):
        try:
            # 尝试获取数据库的元数据
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            logger.info(str(current_datetime) + " " + f"Database tables: {tables}")
            # 执行一个简单的查询
            result = session.execute(text("SELECT 1"))
            logger.info(str(current_datetime) + " " + "Database connection successful.")
            return cookie_service_pb2.CookieResponse(status="success", message="Connection successful.")
        except OperationalError as e:
            logger.error(str(current_datetime) + " " + f"Database connection failed: {e}")
            return cookie_service_pb2.CookieResponse(status="error", message="Connection failed.")
        finally:
            session.close()

    
    # 获取 Cookie 信息通过 ID
    def GetCookieByID(self, request, context):
        try:
            cookie = session.query(Cookie).filter(Cookie.id == request.id).first()
            if cookie:
                logger.info(str(current_datetime) + " " + f"Cookie_GetCookieByID found: {cookie.name}")
                return cookie_service_pb2.CookieResponse_ByID(name=cookie.name, email=cookie.email)
            else:
                logger.info(str(current_datetime) + " " + "Cookie_GetCookieByID not found.")
                return cookie_service_pb2.CookieResponse_ByID(name="Not found", email="Not found")
        except SQLAlchemyError as e:
            logger.error(str(current_datetime) + " " + f"Error: {e}")
            return cookie_service_pb2.CookieResponse_ByID(name="Error", email=str(e))

    # 获取 Cookie 信息通过 Name
    def GetCookieByName(self, request, context):
        try:
            cookie = session.query(Cookie).filter(Cookie.name == request.name).first()
            if cookie:
                logger.info(str(current_datetime) + " " + f"Cookie_GetCookieByName found: {cookie.id}")
                return cookie_service_pb2.CookieResponse_ByName(id=cookie.id, email=cookie.email)
            else:
                logger.info(str(current_datetime) + " " + "Cookie_GetCookieByName not found.")
                return cookie_service_pb2.CookieResponse_ByName(id=-1, email="Not found")
        except SQLAlchemyError as e:
            logger.error(str(current_datetime) + " " + f"Error: {e}")
            return cookie_service_pb2.CookieResponse_ByName(id=-1, email=str(e))

    # 获取 Cookie 信息通过 Email
    def GetCookiesByEmail(self, request, context):
        try:
            cookies = session.query(Cookie).filter(Cookie.email == request.email).all()
            if cookies:
                result = [cookie_service_pb2.CookieInfo(id=cookie.id, name=cookie.name) for cookie in cookies]
                logger.info(str(current_datetime) + " " + f"Cookie_GetCookiesByEmail found: {result}")
                return cookie_service_pb2.CookieResponse_ByEmail(cookies=result)
            else:
                logger.info(str(current_datetime) + " " + "Cookie_GetCookiesByEmail not found.")
                return cookie_service_pb2.CookieResponse_ByEmail(cookies=[])
        except SQLAlchemyError as e:
            logger.error(str(current_datetime) + " " + f"Error: {e}")
            return cookie_service_pb2.CookieResponse_ByEmail(cookies=[])

def serve():
    # 创建 gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 注册服务
    cookie_service_pb2_grpc.add_CookieServiceServicer_to_server(CookieService(), server)

    # 启用反射服务
    # 手动设置反射服务名
    SERVICE_NAMES = (
        cookie_service_pb2_grpc.CookieService.__name__,  # 服务的名字
        reflection.SERVICE_NAME,  # 反射服务
    )

    # 启用反射
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    # 启动 gRPC 服务并监听 50051 端口
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()

    # 保持服务运行
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()