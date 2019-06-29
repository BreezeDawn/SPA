from datetime import datetime

from SPA_back.src.py import db


class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class DataOne(BaseModel, db.Model):
    __tablename__ = 'data_one'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')

    data = db.Column(db.Integer, comment="Data")


class DataTwo(BaseModel, db.Model):
    __tablename__ = 'data_two'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')

    data = db.Column(db.Integer, comment="Data")
