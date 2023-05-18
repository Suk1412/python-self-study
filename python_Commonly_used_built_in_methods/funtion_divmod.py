#!/usr/bin/python3
# -*- encoding: utf-8 -*-


data = input('输入：')
code = compile(f'{data}', '<string>', 'single')
exec(code)


