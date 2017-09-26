# coding=utf-8

from flask import Flask


def create_app():
    """ 工厂方法返回app """
    app = Flask(__name__)
    # 注册蓝图
    from .convert import convert as convert_blueprint
    app.register_blueprint(convert_blueprint)

    return app
