import datetime
import hashlib

from sqlalchemy import Column, DateTime, String, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, SMALLINT, TEXT, INTEGER

from recommendation.dao.db_tools import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'schema': 'poem'
    }

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="用户id")
    user_name = Column(VARCHAR(32), default="", comment="用户名")
    nick_name = Column(VARCHAR(32), default="", comment="昵称")
    province = Column(VARCHAR(128), default="", comment="省")
    city = Column(VARCHAR(128), default="", comment="城市")
    avatar = Column(VARCHAR(32), default="", comment="头像")
    birthday = Column(DateTime, default="", comment="生日")
    gender = Column(SMALLINT, default=0, comment="性别[0-未填写，1-男，2-女，3-其他]")
    description = Column(String(150), comment="描述")
    phone = Column(VARCHAR(32), unique=True, comment="国家码+电话号码")
    email = Column(VARCHAR(100), default="", unique=True, comment="邮箱")
    device_id = Column(CHAR(36), default="", comment="设备id")
    ip = Column(VARCHAR(45), default="", comment="用户ip地址")
    create_time = Column(DateTime(6), default="", comment="注册时间")


class Poem(BaseModel):
    __tablename__ = 'poem'

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'schema': 'poem'
    }

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="诗词id")
    type = Column(SMALLINT, nullable=True, comment="类型：暂未分类0，诗1，词2，曲3，赋4，文5")
    name = Column(VARCHAR(128), default="", comment="标题")
    poet_id = Column(INTEGER, comment="诗人id")
    poet_name = Column(VARCHAR(128), default="", comment="诗人名字")
    dynasty = Column(VARCHAR(128), comment="朝代")
    picture = Column(VARCHAR(32), default="", comment="诗词对应图像")
    content = Column(TEXT, default="", comment="内容")
    md5 = Column(CHAR(32), unique=True, comment="内容md5")
    strains = Column(TEXT, default="", comment="诗的平仄或者词谱；限制")
    fanyi = Column(TEXT, default="", comment="翻译")
    shangxi = Column(TEXT, default="", comment="赏析")
    star = Column(INTEGER, comment="点赞数")
    tags = Column(TEXT, default="", comment="标签")
    about = Column(TEXT, default="", comment="其他相关信息")
    source = Column(VARCHAR(128), comment="来源")
    update_time = Column(DateTime, default=datetime.datetime.now(), comment="更新时间")
    create_time = Column(DateTime, default=datetime.datetime.now(), comment="创建时间")

    def __init__(self, **kwargs):
        super(Poem, self).__init__(**kwargs)
        self.md5 = hashlib.md5(self.content.strip().encode("utf-8")).hexdigest()
        # do custom initialization here

    # def __hash__(self):
    #     return


class Poet(BaseModel):
    __tablename__ = 'poet'

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'schema': 'poem'
    }
    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="诗人id")
    name = Column(VARCHAR(128), default="", comment="诗人名字", index=True)
    zi = Column(VARCHAR(32), default="", comment="诗人的字")
    hao = Column(VARCHAR(128), default="", comment="诗人的号。多个号以半角;分开")
    dynasty = Column(VARCHAR(128), default="", comment="朝代", index=True)
    image = Column(VARCHAR(128), default="", comment="诗人图像")
    birthday = Column(VARCHAR(128), default="", comment="出生时间")
    death = Column(VARCHAR(128), default="", comment="逝世时间")
    gender = Column(SMALLINT, default=0, comment="性别[0-未填写，1-男，2-女，3-其他]")
    city = Column(VARCHAR(128), default="", comment="出生地或成长地")
    star = Column(INTEGER, default=0, comment="诗人总的获赞数")
    tags = Column(TEXT, default="", comment="标签")
    description = Column(TEXT, default="", comment="描述")
    about = Column(TEXT, default="", comment="其他相关信息")
    source = Column(VARCHAR(128), default="", comment="来源")
    update_time = Column(DateTime, default=datetime.datetime.now(), comment="更新时间")
    create_time = Column(DateTime, default=datetime.datetime.now(), comment="创建时间")
    UniqueConstraint(name, zi, hao, dynasty, city)

    def __init__(self, **kwargs):
        super(Poet, self).__init__(**kwargs)


class History(BaseModel):
    __tablename__ = 'history'

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'schema': 'poem'
    }

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="id")
    user_id = Column(INTEGER, nullable=False, comment="user id")
    poem_id = Column(INTEGER, nullable=False, comment="poem id")
    ip = Column(CHAR(20), default="", comment="ip地址")
    weather = Column(VARCHAR(512), default="", comment="天气情况")
    addr = Column(VARCHAR(512), default="", comment="所在位置")
    star = Column(SMALLINT, nullable=False, default=0, comment="是否点赞")
    reason = Column(CHAR(50), default="", comment="数据生成原因")
    type = Column(SMALLINT, nullable=False, comment="数据是真是假")
    create_time = Column(DateTime, default=datetime.datetime.now(), comment="创建时间")
    UniqueConstraint(user_id, poem_id)

    def __init__(self, **kwargs):
        super(History, self).__init__(**kwargs)


def create_all():
    from recommendation.dao.db import mysql_db_engine
    BaseModel.metadata.create_all(mysql_db_engine)  # 创建表
    # BaseModel.metadata.create_all(sqlite_db_engine)  # 创建表
