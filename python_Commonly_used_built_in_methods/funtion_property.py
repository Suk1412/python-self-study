#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 创建可管理的属性。
# 可管理的属性是指可以通过类的方法访问的属性，而不是直接访问类的属性。这允许类设计者灵活地控制类属性的访问和修改方式，从而提高代码的安全性和可维护性。

class MyClass:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        """Getter method for the `x` property."""
        return self._x

    @x.setter
    def x(self, value):
        """Setter method for the `x` property."""
        self._x = value


obj = MyClass()
print(obj.x)
obj.x = 4
print(obj.x)