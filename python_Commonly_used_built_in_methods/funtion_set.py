#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# set()是一个内置函数，用于创建一个集合对象。集合是一种无序、不重复的数据结构，可以用于快速地检查成员资格，删除重复数据等。
# set()可以接受一个可迭代对象作为输入，例如列表、元组或字符串，并返回一个包含所有唯一元素的集合。
a = set([1, 2, 3])
b = set("hello")
print(a) # 输出 {1, 2, 3}
print(b) # 输出 {'l', 'e', 'h', 'o'}

a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.intersection(b) # 计算交集
d = a.union(b)        # 计算并集
e = a.difference(b)   # 计算差集
f = a.symmetric_difference(b) # 计算对称差
print(c, d, e, f)