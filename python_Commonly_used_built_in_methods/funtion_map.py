#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 将一个函数应用于一个或多个序列中的每个元素，并返回一个包含结果的迭代器。
# map(function, iterable, ...)
# 将列表中的每个数乘以2
my_list = [1, 2, 3, 4]
result = map(lambda x: x * 2, my_list)
print(list(result)) # 输出: [2, 4, 6, 8]

# 同时将两个列表中的元素相加
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result)) # 输出: [5, 7, 9]