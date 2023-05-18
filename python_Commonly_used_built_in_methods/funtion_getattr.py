#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 用于获取对象的属性值。
"""
getattr(object, name[, default])
    object 是要获取属性值的对象
    name 是属性名
    default 是可选参数
"""

class MyClass:
    def __init__(self):
        self.my_attribute = 'hello'

my_object = MyClass()
my_value = getattr(my_object, 'my_attribute')
print(my_value)

# 使用默认值获取对象的属性值
default_value = 'world'
non_existent_value = getattr(my_object, 'non_existent_attribute', default_value)
print(non_existent_value) # 输出: world