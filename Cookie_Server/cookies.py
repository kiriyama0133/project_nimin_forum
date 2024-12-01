from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker,declarative_base
from sqlalchemy import Column, Text, Integer,String, VARCHAR, TIMESTAMP, BOOLEAN, Float, text
from sqlalchemy.exc import SQLAlchemyError
import random
import string
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, redirect, url_for, request, render_template
from sqlalchemy.exc import OperationalError
from datetime import datetime
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

# 创建数据库引擎（SQLite 示例）
engine = create_engine('sqlite:///cookies.db')
# 创建表
Base.metadata.create_all(engine)

#数据库连接配置
DATABASE_URL = "sqlite:///cookies.db"
engine = create_engine(DATABASE_URL, echo=True)

#创建数据库会话
Session=sessionmaker(bind=engine)
session=Session()

app = Flask(__name__)
@app.route('/test')
# 检测数据库连接
def check_db_connection():
    try:
        # 尝试获取数据库的元数据
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        logger.info(str(current_datetime)+" "+"Database tables: %s", tables)

        # 尝试执行一个简单的查询
        result = session.execute(text("SELECT 1"))
        logger.info(str(current_datetime)+" "+"Database connection successful.")
        return True
    except OperationalError as e:
        logger.error(str(current_datetime)+" "+f"Database connection failed: {e}")
        return False
    finally:
        session.close()

# 测试数据库连接
if check_db_connection():
    logger.info(str(current_datetime)+" "+"Database is ready to use.")
else:
    logger.error(str(current_datetime)+" "+"Database is not available.")

@app.route('/delate/<_name>')
# 删除操作
def delete_cookie(_name):
    try:
        user_to_delete = session.query(Cookie).filter(Cookie.name == _name).first()
        print(user_to_delete)
        session.delete(user_to_delete)
        session.commit()
        return "yes"
    except Exception as e:
        logger.warning(e)
        return "error"

def generate_random_string(length=7):
    # 生成一个包含大小写字母的字符串
    letters = string.ascii_letters  # 包含所有大小写字母
    random_string = ''.join(random.choice(letters) for _ in range(length))
    if query_cookie(random_string)=="yes":  # 如果随机字符串已经存在，则重新生成
        generate_random_string()
    return random_string

@app.route('/add')
# 添加操作
def add_cookie():
    try:
        new_cookie = Cookie(
            name=generate_random_string(),
            used=False,
            email="___"
        )
        session.add(new_cookie)
        session.commit()
        session.close()
        logger.info(str(current_datetime)+" "+Cookie.name+"Cookie added successfully.")
    except Exception as e:
        logger.warning(str(current_datetime)+" "+e)

@app.route('/query/<_name>')
# 定义查询函数
def query_cookie(_name):
    try:
        # 使用 exists() 查询是否存在该记录
        cookies = session.query(Cookie).filter(Cookie.name == _name).first()  # 使用 first() 获取结果
        if cookies:  # 如果有记录，返回 True
            logger.info(str(current_datetime)+" "+_name+" "+"Cookie found.")
            return "yes"
        else:  # 没有记录，返回 False
            logger.info(str(current_datetime)+" "+_name+" "+"Cookie not found.")
            return "false"
    except SQLAlchemyError as e:
        # 错误处理
        logger.warning(f"查询出错: {str(e)}")
        return False

if __name__ == '__main__':
    check_db_connection()
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run()
