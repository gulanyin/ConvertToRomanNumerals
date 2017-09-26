# coding=utf-8


def convert_to_roman_numerals(num):
    """
    返回1-100之间的整数的罗马数字形式
    :param num:1-100之间的整数
    :return:罗马数字形式
    """
    if not isinstance(num, int):
        raise Exception("The input must be integers")
    if num < 1 or num > 100:
        raise Exception("The input must be between 1-100")

    num_list = [100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_list = ["C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ''
    for i in range(len(num_list)):
        while num >= num_list[i]:
            num -= num_list[i]
            result += roman_list[i]

    return result
