# -*- coding: utf-8 -*- 
# @Time : 2020/8/2 13:14 
# @Author : sml 
# @File : 9.矩形覆盖.py 

"""我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？"""
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        fOne = 1
        fTwo = 2
        for i in range(3,number+1):
            fN = fTwo + fOne
            fOne = fTwo
            fTwo = fN
        return  fN

