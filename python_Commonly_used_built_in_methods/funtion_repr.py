#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 一个内置函数，用于返回一个对象的字符串表示形式
# repr()函数通常用于调试和开发期间，它可以将对象转换为可打印的字符串，以便查看对象内容或调试错误。

a = [1, 2, 3]
b = "hello"
c = {'name': 'Alice', 'age': 30}

print(repr(a)) # 输出 '[1, 2, 3]'
print(repr(b)) # 输出 "'hello'"
print(repr(c)) # 输出 "{'name': 'Alice', 'age': 30}"