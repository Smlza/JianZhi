# -*- coding: utf-8 -*- 
# @Time : 2020/8/12 23:16 
# @Author : sml 
# @File : 28.最小的k个数.py 
"""
题目描述
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        l=[]
        for i in tinput:
            l.append(i)
        l.sort()
        length=len(l)

        if k>length:
            return []

        else:
            return l[:k]
if __name__ == '__main__':
    tinput=[4,1,3,6,7,8]
    k=2
    f=Solution()
    print(f.GetLeastNumbers_Solution(tinput,k))



