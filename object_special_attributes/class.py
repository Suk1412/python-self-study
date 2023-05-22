#!/usr/bin/python3
# -*- encoding: utf-8 -*-
class MyClass(object):
    # 构造函数或初始化方法:创建类实例时自动调用，用来执行一些初始化操作。
    """
        help文档帮助
    """
    def __init__(self, name='wangxiao', age=20, *args, **kwargs):
        self.attribute1 = 1
        self.attribute2 = 2
        self.attribute3 = 'Hello'
        self.attribute4 = 'word!'
        self.attribute5 = [1, 2, 3]
        self.name = name
        self.age = age


    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.attribute1 == other.attribute1
        return False

    def __format__(self, format_spec):
        if format_spec == "s":
            return f"{self.name} {self.age}"
        elif format_spec == "r":
            return f"{self.name[::-1]} {self.age}"
        else:
            return str(self)

    # 用于实现对象的“大于等于”比较操作
    def __ge__(self, other):
        print(other.age)
        return self.age >= other.age

    # 获得类名
    def get_class_name(self):
        return self.__class__.__name__


    @classmethod
    def print_name(cls, arg1):
        print(f'{str(arg1)}:{cls.__name__}')
        cls.attribute7 =arg1


obj = MyClass()

# 表示对象的类
obj.__class__

# 删除对象属性
obj.__delattr__('attribute4')

# 返回一个字典：对象的所有属性
obj.__dict__

# 返回一个列表：包含了类或实例的所有可访问属性、方法、类变量等信息
obj.__dir__()

# 返回一个字符串：用于获取对象的文档字符串
obj.__doc__


# __eq__ 判断两个对象是否相等
obj2 = MyClass(attribute1='Alice')
obj3 = MyClass(attribute1='Alice')

# __format__ 用于自定义格式化字符串的方式
obj4 = MyClass(name='wangxiao', age=11)
result = "{:s}".format(obj4)

# __ge__
age1 = MyClass(age=20)
age2 = MyClass(age=30)
age1 <= age2


print(dir(obj))
