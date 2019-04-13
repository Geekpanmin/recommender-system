from sqlalchemy import Column, DateTime, String, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, SMALLINT

from recommendation.dao.db_tools import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'schema': 'user'
    }

    id = Column(CHAR(36), primary_key=True, comment="用户id")
    user_name = Column(VARCHAR(32), default="", comment="用户名")
    nick_name = Column(VARCHAR(32), default="", comment="昵称")
    password = Column(VARCHAR(128), comment="密码")
    avatar = Column(VARCHAR(32), default="", comment="头像")
    birthday = Column(DateTime, default="", comment="生日")
    gender = Column(SMALLINT, default=0, comment="性别[0-未填写，1-男，2-女，3-其他]")
    description = Column(String(150), comment="描述")
    phone = Column(VARCHAR(32), unique=True, comment="国家码+电话号码")
    email = Column(VARCHAR(100), default="", comment="邮箱")
    status = Column(SMALLINT, default=0, comment="状态")
    device_id = Column(CHAR(36), default="", comment="设备id")
    ip = Column(VARCHAR(45), default="", comment="用户ip地址")
    geo_location = Column(VARCHAR(128), default="", comment="地理定位经纬坐标")
    geo_country = Column(VARCHAR(128), default="", comment="定位国家")
    last_login_time = Column(DateTime(6), default="", comment="上次登录时间")
    create_time = Column(DateTime(6), default="", comment="注册时间")
    UniqueConstraint(user_name, )


def create_all():
    from recommendation.dao.db import mysql_db_engine, sqlite_db_engine
    BaseModel.metadata.create_all(mysql_db_engine)  # 创建表
    BaseModel.metadata.create_all(sqlite_db_engine)  # 创建表
