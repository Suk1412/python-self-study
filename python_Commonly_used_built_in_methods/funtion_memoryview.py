#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# 将一个对象转换为内存视图对象，该内存视图对象允许直接访问对象的内存表示形式。

# 创建一个字节数组并转换为内存视图对象
buf = bytearray(b'hello')
mv = memoryview(buf)

# 读取和修改内存视图中的数据
print(mv[1]) # 输出: 101
mv[0] = 104
print(mv[0]) # 输出: 104

print(buf)   # 输出: bytearray(b'hello')
print(mv)    # 输入: <memory at 0x7feb1cb641c8>