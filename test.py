#!/usr/bin/enc python
#coding:utf-8
value = 'aaa'
b = value
print(id(value))
value = '5'
print(id(value))
print(id(b))
print(b)