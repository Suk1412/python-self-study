#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 将一个字符串或数字转换为整数。
int(x=0, base=10)
# 将字符串转换为整数
my_string = '123'
my_int = int(my_string)
print(my_int) # 输出: 123

# 将二进制字符串转换为整数
my_string = '0b1010'
my_int = int(my_string, 2)
print(my_int) # 输出: 10

# 将八进制字符串转换为整数
my_string = '0o12'
my_int = int(my_string, 8)
print(my_int) # 输出: 10

# 将十六进制字符串转换为整数
my_string = '0xA'
my_int = int(my_string, 16)
print(my_int) # 输出: 10
