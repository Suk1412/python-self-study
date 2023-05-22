#!/usr/bin/python3
# -*- encoding: utf-8 -*-


# 获取 MyClass 的所有方法和属性

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self):
        pass

    def bar(self, z):
        pass

print(dir(MyClass))