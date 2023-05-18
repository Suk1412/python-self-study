#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 用于判断一个对象是否包含指定的属性。

"""hasattr(object, name)"""

# 检查对象是否包含指定的属性
class MyClass:
    def __init__(self):
        self.my_attribute = 'hello'

my_object = MyClass()
print(hasattr(my_object, 'my_attribute')) # 输出: True
print(hasattr(my_object, 'non_existent_attribute')) # 输出: False