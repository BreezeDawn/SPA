import os
import logging
import configparser

from SPA_back.src.py import BASE_DIR


class Config:
    DEBUG = True

    SECRET_KEY = "DxY3z7jndzYaiY1ndZh+OJOv800zHpRZiWwwNBjC5PAQ1IEMMcWqiyQ8xn2lviMg"

    # sqlalchemy.config
    sql_config_path = os.path.join(BASE_DIR, "py", "config", "sql.ini")

    config = configparser.ConfigParser()

    config.read(sql_config_path, "utf-8")

    sql_config = list(dict(config.items("mysql")).values())

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(*sql_config)

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    """
    定义开发环境的配置
    """
    DEBUG = True
    LOGLEVEL = logging.DEBUG
    JSON_AS_ASCII = False


class ProductConfig(Config):
    """
    定义生产环境的配置
    """
    DEBUG = False
    LOGLEVEL = logging.ERROR


# 设置配置字典
config_dict = {
    "dev": DevelopConfig,
    "pro": ProductConfig
}
