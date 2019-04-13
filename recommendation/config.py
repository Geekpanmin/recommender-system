import os
from local_config import LocalConfig

base_dir = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(base_dir, "data")

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

sqlite_poem_db_path = os.path.join(data_dir, "poem.sqlite")
sqlite_db_host = ""  # 本机相对路径


class Config(LocalConfig):
    sqlite_conf = {
        "host": sqlite_db_host,
        "db_path": sqlite_poem_db_path
    }

    mysql_conf = LocalConfig.mysql_conf


config = Config()
__all__ = ["config"]
