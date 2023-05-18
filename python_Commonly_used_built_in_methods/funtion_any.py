#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 接受一个可迭代对象作为参数，有一个True,则返回True，否则返回False
value = [0, 1, 2]
value1 = [0, None]

print(any(value))
print(any(value1))