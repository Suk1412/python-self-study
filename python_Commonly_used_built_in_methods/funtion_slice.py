#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# Python内置函数，用于创建一个表示切片的对象，它可以作为切片操作符[]的参数。

my_list = [0, 1, 2, 3, 4, 5]
s = slice(1, 5, 2)
print(my_list[s])   # 输出 [1, 3]