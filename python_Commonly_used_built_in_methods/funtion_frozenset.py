#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 回一个不可变的集合对象，即冻结集合。
"""
frozenset([iterable])
"""

# 创建冻结集合
my_set = {1, 2, 3}
my_frozen_set = frozenset(my_set)
print(my_frozen_set) # 输出: frozenset({1, 2, 3})

# 尝试修改冻结集合
try:
    my_frozen_set.add(4)
except AttributeError as e:
    print(e) # 输出: 'frozenset' object has no attribute 'add'
