# -*- coding: utf-8 -*- 
# @Time : 2020/8/1 16:05 
# @Author : sml 
# @File : 7.跳台阶.py
"""

题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

题目解析
这是一道经典的递推题目，你可以想如果青蛙当前在第n级台阶上，那它上一步是在哪里呢？

显然，由于它可以跳1级台阶或者2级台阶，所以它上一步必定在第n-1,或者第n-2级台阶，
也就是说它跳上n级台阶的跳法数是跳上n-1和跳上n-2级台阶的跳法数之和。

"""
class Solution:
    def jumpFloor(self, number):
        if number ==1:
            return 1
        elif number==2:
            return 2
        else:
            s=[1,2]
            for i in range(2,number+1):
                a=s[i-1]+s[i-2]
                s.append(a)
            return s[number-1]





