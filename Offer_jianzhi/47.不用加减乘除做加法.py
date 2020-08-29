# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 10:19 
# @Author : sml 
# @File : 47.不用加减乘除做加法.py 

"""
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
class Solution:
    def Add(self, num1, num2):
        # write code here
        l=[]
        l.append(num1)
        l.append(num2)
        return sum(l)

