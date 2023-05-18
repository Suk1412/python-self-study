#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 用来指示一个方法是类方法 使用@classmethod
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count += 1
        print('创建一个实例对象')

    @classmethod
    def get_count(cls):
        return cls.count

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count()) # 输出 2


# 貌似可以用这个方法做单例类
# obj1 = None
# for i in range(10):
#     if MyClass.get_count() < 1:
#         obj1 = MyClass()
#         print(type(obj1))
#     else:
#         print('已有实例对象，不创建')
#         obj1 = obj1
#         print(type(obj1))

