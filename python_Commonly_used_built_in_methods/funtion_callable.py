#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 用于检查一个对象是否是可调用的（即能否被调用执行）。如果对象可以被调用，返回 True；否则返回 False。
# 在 Python 中，函数、方法、生成器函数、类以及实现了 __call__() 方法的对象都属于可调用对象。而其他类型的对象则不是可调用的，例如数字、字符串、元组、列表等。

def my_func():
    print("Hello, World!")

class MyClass:
    def __init__(self):
        pass

    def __call__(self):
        print("I am being called!")

obj = MyClass()

print(callable(my_func))  # 输出 True
print(callable(obj))  # 输出 True
print(callable(123))  # 输出 False
print(callable("hello"))  # 输出 False