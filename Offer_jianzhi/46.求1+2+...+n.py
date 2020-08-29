# -*- coding: utf-8 -*- 
# @Time : 2020/8/22 21:56 
# @Author : sml 
# @File : 46.求1+2+...+n.py 

"""
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

考虑用递归
"""
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        s = n
        flag = s and self.Sum_Solution(n-1)
        return s+flag


