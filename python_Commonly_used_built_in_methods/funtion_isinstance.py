#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 检查一个对象是否是某个类或其子类的实例。
# isinstance(object, classinfo)


# 定义一个基类和一个子类
class Animal:
    pass

class Cat(Animal):
    pass

# 创建一个 Cat 类型的对象
my_cat = Cat()

# 使用 isinstance() 检查对象的类型
print(isinstance(my_cat, Animal)) # 输出: True
print(isinstance(my_cat, Cat))    # 输出: True
print(isinstance(my_cat, object)) # 输出: True