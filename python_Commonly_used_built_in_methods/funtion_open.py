#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# file是要打开的文件路径和名称；mode指定文件的打开模式，默认为只读模式（'r'）；buffering控制是否缓冲；encoding指定文本文件的编码方式；errors指定编码错误处理方式；newline指定换行符的转换方式。
file = 'example.txt'
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 打开一个文本文件并读取内容
with open('example.txt', 'r') as file:
    content = file.read()

# 打开一个文本文件并按行读取内容
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 创建一个新文本文件并写入内容
with open('new_file.txt', 'w') as file:
    file.write('Hello, world!')