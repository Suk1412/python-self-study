#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 用于获取一组值或一个可迭代对象中的最大值。

# 获取一组数字中的最大值
print(max(1, 2, 3, 4, 5)) # 输出: 5

# 获取一个列表中的最大值
my_list = [7, 3, 9, 2, 8]
print(max(my_list)) # 输出: 9

# 获取一个元组中的最大值
my_tuple = (10, 20, 30)
print(max(my_tuple)) # 输出: 30

# 获取一个字符串中的最大字符
my_string = 'hello'
print(max(my_string)) # 输出: '0'

# 按照字符串长度获取一个列表中的最大字符串
my_list = ['apple', 'banana', 'pear']
print(max(my_list, key=len)) # 输出: 'bananan'