#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# reversed()是一个内置函数，用于反转序列对象（字符串、列表、元组等）中的元素顺序。
a = [1, 2, 3]
b = reversed(a)
print(list(b)) # 输出 [3, 2, 1]