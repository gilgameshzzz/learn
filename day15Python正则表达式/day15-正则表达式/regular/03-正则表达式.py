"""__author__ = 余婷"""
"""
1.特殊符号转义
正则中：. \ [] {} () * + ? ^ $ | 这些字符有特殊意义，所以在正则表达式中，
       如果想要单纯表达这些字符，需要在前面加'\'; 
       
       
注意：1. -，[],^,\ 在中括号中可能是特殊的符号,需要加\
     2. . {} () * + ? $ |在中括号中可以不用加\,来表示字符
"""

import re

if __name__ == '__main__':
    re_str = r'\d+[1\-3]\d+'
    print(re.fullmatch(re_str, '12-89'))

    re_str = r'[\^]'  # 匹配 字符^
    re_str = r'[\\]'  # 匹配 字符\
    re_str = r'[\$]'
    re_str = r'[{}]'
    print(re.fullmatch(re_str, '{'))

    # 1. \N --> 匹配前面第N个组中匹配到的内容
    re_str = r'([1-9][a-z]{2})n(\d)\1\2'
    print(re.fullmatch(re_str, '9hjn09hj0'))



    # 练习1.
    # 用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    re_str = r'\w{6,20}'
    #QQ号是5~12的数字且首位不能为0
    re_str = r'[1-9]\d{4,11}'

    # 练习2：IP地址是合法
    """
    x.x.x.x
    x: 1-255
    写一个正则表达式判断一个字符串是否是：1-255
    1-9
    10-99
    100-199
    200-249
    250-255
    """
    re_str = r'(([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])'
    print(re.fullmatch(re_str, '10.7.1.249'))

