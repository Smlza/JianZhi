# -*- coding: utf-8 -*- 
# @Time : 2020/8/2 14:01 
# @Author : sml 
# @File : 10.二进制中1的个数.py 
"""
题目描述
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

思路：1.正数的补码反码就是原码，负数的补码是反码加1
     2.n=n&0xffffffff，求负数n的补码形式
     3.使用n=n&n-1来统计1的个数
"""


class Solution:
    def NumberOf1(self, n):
        if n==0:
            return 0
        elif n<0:
            n=n&0xffffffff
        count=0
        while n:
            count+=1
            n=n&n-1
        return count

# write code here
s=Solution()
print(s.NumberOf1(n=-1))