# -*- coding: utf-8 -*- 
# @Time : 2020/8/3 19:33 
# @Author : sml 
# @File : 11.数值的整数次方.py 
# 题目描述
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#
# 保证base和exponent不同时为0
"""思路：考虑base与exponent是否为0
        考虑exponent的正负，负数取得是倒数
"""
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag=0
        if base ==0:
            return False
        if exponent ==0:
            return 1

        if exponent<0:
            flag=1
        result = 1
        for i in range(abs(exponent)):
            result*=base
        if flag==1:
            result=1/result
        return result


