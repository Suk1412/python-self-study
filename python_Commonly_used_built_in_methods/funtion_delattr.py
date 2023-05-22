#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 一种内置函数，用于删除对象的属性。该函数接受两个参数：一个是要删除属性的对象，另一个是要删除的属性的名称。
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(10,20)
delattr(obj, 'x')