# -*- coding: utf-8 -*- 
# @Time : 2020/8/25 15:33 
# @Author : sml 
# @File : 55.链表中环的入口节点.py 

"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
def wa(func):
    def f():
        print("1")
        func()
        print("2")
    return f

@wa #f1=wa(f1)
def f1():
    print(3)

f1()

