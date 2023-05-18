#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 将一个可迭代对象转换为列表。


# 将元组转换为列表
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list) # 输出: [1, 2, 3, 4, 5]

# 将字符串转换为列表
my_string = 'hello'
my_list = list(my_string)
print(my_list) # 输出: ['h', 'e', 'l', 'l', 'o']

# 将字典的键转换为列表
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = list(my_dict.keys())
print(my_list) # 输出: ['a', 'b', 'c']
