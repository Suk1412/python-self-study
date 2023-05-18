#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 用于从迭代器中获取下一个元素

# 创建一个列表并获取其中的元素
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter)) # 输出: 1
print(next(my_iter)) # 输出: 2
print(next(my_iter)) # 输出: 3