# coding=utf-8


class ResponseError(Exception):
    """
        异常错误响应类
    """

    # 发生异常错误默认的http响应状态码
    status_code = 400

    # 自定义 return_code，作为更细颗粒度的错误代码
    def __init__(self, error_code=None, status_code=None, message=None):
        """
        初始化异常响应类
        :param error_code: 自定义错误代码
        :param status_code: 响应状态码
        :param message:
        """
        Exception.__init__(self)
        self.error_code = error_code
        if status_code is not None:
            self.status_code = status_code
        self.message = message

    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict()
        # 增加 dict key: error code
        rv['error_code'] = self.error_code
        # 增加 dict key: message
        rv['message'] = self.message

        return rv
