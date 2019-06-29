import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# 将数据库操作对象全局化 方便其他文件操作数据库
db = None  # type: SQLAlchemy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from SPA_back.src.py.config.config import config_dict


def create_app(config_type):
    # 根据配置类型取出配置类
    config_class = config_dict[config_type]
    app = Flask(__name__)

    app.config.from_object(config_class)
    app.template_folder = '../templates'
    app.config['JSON_AS_ASCII'] = False

    global db

    db = SQLAlchemy(app)

    Migrate(app, db)

    from SPA_back.src.py.services.DataService import data_blue
    app.register_blueprint(data_blue)

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"code": "404", "message": str(e)})

    CSRFProtect(app)
    CORS(app, supports_credentials=True)

    from SPA_back.src.py.services.DataService import models

    return app
