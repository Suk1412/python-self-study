#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 创建一个不可变字节数组
value = 0
value1 = 7
value2 = None
value3 = 'hello'

def run(value):
    value_1 = None
    if not value:
        print('传值为None')
    else:
        if isinstance(value, int):
            print(f'原值:{value}\t\t原值类型:{type(value)}')
            value_1 = bytes(value)
        elif isinstance(value, str):
            print(f'原值:{value}\t\t原值类型:{type(value)}\t\t原值长度:{len(str(value))}')
            value_1 = bytes(value, 'utf-8')
        else:
            print('意外输入！！！')
        print(f'转换后值:{value_1}\t\t转换后类型:{type(value_1)}\t\t转换后长度:{len(value_1)}')
    return value_1


run(value)
print('--'*30)
run(value1)
print('--'*30)
run(value2)
print('--'*30)
run(value3)

