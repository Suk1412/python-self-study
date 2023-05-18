#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 返回当前局部作用域中所有变量的字典。这些变量包括当前函数或方法的参数、局部变量和导入的模块。
# locals() 函数没有参数，调用它时会返回一个字典，其中包含了当前作用域中所有变量的名称和值。这个字典可以被修改，但这并不会改变实际的变量绑定关系。

def example_function(x, y):
    z = x + y
    h = x**y
    print(locals())

example_function(2, 3)