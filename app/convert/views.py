# coding=utf-8
from flask import jsonify

from app.ResponseError import ResponseError
from tool.NumberConvert import convert_to_roman_numerals
from . import convert


@convert.errorhandler(ResponseError)
def handle_flask_error(error):

    # response 的 json 内容为自定义错误代码和错误信息
    response = jsonify(error.to_dict())

    # response 返回 error 发生时定义的标准错误代码
    response.status_code = error.status_code

    return response


@convert.route('/convert/<int:num>')
def convert(num):
    # 不在1-100之间返回错误代码400，错误信息：The input must be between 1-100，http响应状态码400
    if num < 1 or num > 100:
        raise ResponseError(error_code=400, message='The input must be between 1-100')

    result = convert_to_roman_numerals(num)
    return jsonify({"result": result})
