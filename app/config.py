# _*_ coding:utf-8 _*_

"""
项目配置项
write the code, change the world
"""

__author__ = "openchina"

__time__ = "2019.01.04"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'  # 密钥
# 添加数据库配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1:3306/dbname'  # 配置数据库

db = SQLAlchemy(app)
