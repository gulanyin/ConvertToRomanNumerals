# coding=utf-8
from flask import Blueprint, jsonify


convert = Blueprint('convert', __name__)

# 防止循环导入
from . import views



