# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 12:10 
# @Author : sml 
# @File : 51.构建乘积数组.py 
"""
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
"""
class Solution:
    def multiply(self, A):
        # write code here
        B=[i for i in range(len(A))]
        for i in range(len(A)):
            B[i]=1
            for j in (A[:i]+A[i+1:]):
                B[i]=B[i]*j
        return B

