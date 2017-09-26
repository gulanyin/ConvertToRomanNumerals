# coding=utf-8
import unittest

from tool.NumberConvert import convert_to_roman_numerals


class NumberConvertUnitTest(unittest.TestCase):
    """"
        tool.NumberConvert.convert_to_roman_numerals 函数单元测试类
    """

    # 测试类型
    def test_1_input_must_be_integers(self):
        try:
            convert_to_roman_numerals("string")
        except Exception as e:
            self.assertEqual(str(e), "The input must be integers")

        try:
            convert_to_roman_numerals(3.14)
        except Exception as e:
            self.assertEqual(str(e), "The input must be integers")

    # 测试输入数字范围
    def test_2_input_must_be_between_1_to_100(self):
        try:
            convert_to_roman_numerals(1000)
        except Exception as e:
            self.assertEqual(str(e), "The input must be between 1-100")

        try:
            convert_to_roman_numerals(0)
        except Exception as e:
            self.assertEqual(str(e), "The input must be between 1-100")

    # 测试正确回结果
    def test_3_input_and_return_correct_roman_numerals(self):
        self.assertEqual("V", convert_to_roman_numerals(5))
        self.assertEqual("VII", convert_to_roman_numerals(7))
        self.assertEqual("X", convert_to_roman_numerals(10))
        self.assertEqual("XX", convert_to_roman_numerals(20))
        self.assertEqual("C", convert_to_roman_numerals(100))

if __name__ == '__main__':
    unittest.main()
