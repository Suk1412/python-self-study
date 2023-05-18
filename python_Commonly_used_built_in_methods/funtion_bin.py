#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 接受一个可迭代对象作为参数，有一个True,则返回True，否则返回False
value = 1
value1 = 7


def run(value):
    print(f'原值:{value}\t\t原值类型:{type(value)}\t\t原值长度:{len(str(value))}')
    value_1 = bin(value)
    print(f'转换后值:{value_1}\t\t转换后类型:{type(value_1)}\t\t转换后长度:{len(str(value_1))}')
    return value_1

run(value)
print('--'*30)
run(value1)