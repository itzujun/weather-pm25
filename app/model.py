# _*_ coding:utf-8 _*_
"""
项目配置项
write the code, change the world
"""

__author__ = "openchina"

__time__ = "2019.01.04"

from app.config import db


class CityWeather(db.Model):
    __tablename__ = 'cityweather'
    id = db.Column(db.Integer, primary_key=True)  # ID
    time = db.Column(db.String(32))
    city = db.Column(db.String(128))  # 城市名字
    AQI = db.Column(db.String(32))  # AQI
    quality = db.Column(db.String(8))  # 空气质量
    pm = db.Column(db.String(32))  # pm2.5
