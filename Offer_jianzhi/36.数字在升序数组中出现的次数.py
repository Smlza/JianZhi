# -*- coding: utf-8 -*- 
# @Time : 2020/8/18 22:41 
# @Author : sml 
# @File : 36.数字在升序数组中出现的次数.py 

"""
题目描述
统计一个数字在升序数组中出现的次数。
"""
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        n= data.count(k)
        return n
