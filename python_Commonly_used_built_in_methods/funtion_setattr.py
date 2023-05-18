#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# setattr()是一个内置函数，用于设置对象的属性值.
# 具体来说，setattr()函数接受三个参数：
#     对象obj：要设置属性的对象。
#     字符串name：属性名称。
#     值value：要设置的属性值。


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(10,20)
setattr(obj, 'age', 30)
print(obj.age)
