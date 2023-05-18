#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 检查一个类是否是另一个类的子类。
# issubclass(class, classinfo)

# 定义一个基类和一个子类
class Animal:
    pass

class Cat(Animal):
    pass

# 使用 issubclass() 检查类之间的继承关系
print(issubclass(Cat, Animal)) # 输出: True
print(issubclass(int, object)) # 输出: True
print(issubclass(bool, int))   # 输出: True