# coding=utf-8
import unittest

from app import create_app


class MainConvertUnitTest(unittest.TestCase):
    """
        测试convert.views中的convert视图函数
    """
    def setUp(self):
        self.app = create_app()
        self.app.config['SERVER_NAME'] = 'localhost'
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    # 测试输入字符串
    def test_1_input_is_string(self):
        response = self.client.get("http://localhost/convert/abc")
        self.assertEqual(response.status_code, 404)

    # 测试输入浮点数
    def test_2_input_is_float(self):
        response = self.client.get("http://localhost/convert/3.14")
        self.assertEqual(response.status_code, 404)

    # 测试输入超出1-100的整数
    def test_3_input_is_not_between_in_1_to_100(self):
        response = self.client.get("http://localhost/convert/0")
        self.assertEqual(response.status_code, 400)
        response = self.client.get("http://localhost/convert/101")
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()