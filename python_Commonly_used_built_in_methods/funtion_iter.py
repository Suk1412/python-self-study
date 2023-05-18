#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 用于获取迭代器对象的内置函数。它接收一个可迭代对象作为参数，并返回该对象对应的迭代器。通常用于可以被迭代的对象（例如列表、元组、集合、字符串等）。

my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter))  # 输出 1
print(next(my_iter))  # 输出 2
print(next(my_iter))  # 输出 3
print(next(my_iter))  # 抛出 StopIteration 异常