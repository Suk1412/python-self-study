#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 返回一个数值的绝对方法
value = -10
value1 = 13


def run(value):
    print(f'原值:{value}\t\t原值类型:{type(value)}\t\t原值长度:{len(str(value))}')
    value_1 = abs(value)
    print(f'转换后值:{value_1}\t\t转换后类型:{type(value_1)}\t\t转换后长度:{len(str(value_1))}')
    return value_1

run(value)
print('--'*30)
run(value1)