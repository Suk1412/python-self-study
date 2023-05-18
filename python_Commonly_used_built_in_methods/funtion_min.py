#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 用于获取一组值或一个可迭代对象中的最小值。

# 获取一组数字中的最小值
print(min(1, 2, 3, 4, 5)) # 输出: 1

# 获取一个列表中的最小值
my_list = [7, 3, 9, 2, 8]
print(min(my_list)) # 输出: 2

# 获取一个元组中的最小值
my_tuple = (10, 20, 30)
print(min(my_tuple)) # 输出: 10

# 获取一个字符串中的最小字符
my_string = 'hello'
print(min(my_string)) # 输出: 'e'

# 按照字符串长度获取一个列表中的最小字符串
my_list = ['apple', 'banana', 'pear']
print(min(my_list, key=len)) # 输出: 'pear'