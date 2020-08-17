# -*- coding: utf-8 -*- 
# @Time : 2020/8/16 21:09 
# @Author : sml 
# @File : 31.把数组排成最小的数.py 

"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。

思路：变相冒泡
"""
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        length=len(numbers)
        if not numbers:
            return ''
        l=[str(i) for i in numbers]
        for i in range(length-1):
            for j in range(length-i-1):
                if int(l[j]+l[j+1])>int(l[j+1]+l[j]):
                    l[j],l[j + 1]=l[j+1],l[j]
        min=int(''.join(i for i in l))
        return min






