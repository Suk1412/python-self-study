#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# 返回一个字符串的ASCII表示
value = '你好'
value1 = 13
value2 = 'hell0'

def run(value):
    print(f'原值:{value}\t\t原值类型:{type(value)}\t\t原值长度:{len(str(value))}')
    value_1 = ascii(value)
    print(f'转换后值:{value_1}\t\t转换后类型:{type(value_1)}\t\t转换后长度:{len(str(value_1))}')
    return value_1

run(value)
print('--'*30)
run(value1)
print('--'*30)
run(value2)