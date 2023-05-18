#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 可以用来创建一个空字典，也可以用来从其他可迭代对象（如列表、元组、集合等）创建一个字典。

# 创建一个空字典
my_dict = dict()

# 从两个列表中创建一个字典
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))

# 从元组序列中创建一个字典
my_tuples = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(my_tuples)

