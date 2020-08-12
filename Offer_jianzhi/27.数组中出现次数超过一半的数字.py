# -*- coding: utf-8 -*- 
# @Time : 2020/8/12 22:47 
# @Author : sml 
# @File : 27.数组中出现次数超过一半的数字.py 

"""题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""
# print(5//2)
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here

        l=[]
        for i in numbers:
            l.append(i)
        length=len(l)

        l.sort()
        if length==0:
            return 0
        if length==1:
            return l[0]
        for i in range(length//2):

            if l[i]==l[i+length//2]:
                return l[i]

        return 0





