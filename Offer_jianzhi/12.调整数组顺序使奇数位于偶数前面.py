# -*- coding: utf-8 -*- 
# @Time : 2020/8/3 20:09 
# @Author : sml 
# @File : 12.调整数组顺序使奇数位于偶数前面.py 
"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，
偶数和偶数之间的相对位置不变。
"""
class Solution:
    def reOrderArray(self, array):
        # write code here
        Q=[]
        O=[]
        for i in array:
            if i%2 ==1:
                Q.append(i)
            else:
                O.append(i)
        Q.sort()
        O.sort()
        Q.extend(O)
        return Q