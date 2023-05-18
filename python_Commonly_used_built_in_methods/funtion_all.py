#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 接受一个可迭代对象作为参数，都为True,则返回True，否则返回False
value = [1, 2, 3]
value1 = [0, 1, 2]

print(all(value))
print(all(value1))
