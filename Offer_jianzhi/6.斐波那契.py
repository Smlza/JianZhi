# -*- coding: utf-8 -*- 
# @Time : 2020/8/1 15:43 
# @Author : sml 
# @File : 6.斐波那契.py 

class Solution:
    def Fibonacci(self, n):
        s=[0,1]
        if n==0 :
            return s[0]
        elif n==1:
            return s[1]
        else:
            for i in range(2,n+1):
                k=s[i-1]+s[i-2]
                s.append(k)
        return s[n]

