#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
compile()函数将一个字符串形式的源代码编译成可执行代码或者一个代码对象，并返回编译后的内容。
接受三个参数：source，filename，mode
source：表示要编译的代码字符串
filename：表示代码文件名，通常使用 "<string>" 表示从字符串中读取源代码。
mode：表示编译模式，有三种取值：
    eval：用于执行单个表达式。
    exec：用于执行一组语句（如多行代码）。
    single：用于执行单行语句，也就是交互式控制台中的输入。
"""

code = compile('print("Hello, World!")', '<string>', 'eval')
exec(code)
print('-'*30)
code = compile('print(2 + 2)\nprint("BBA")', '<string>', 'exec')
exec(code)
print('-'*30)
code = compile('2 + 3', '<string>', 'single')
exec(code)
