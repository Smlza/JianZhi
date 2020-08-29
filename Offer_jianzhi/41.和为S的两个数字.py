# -*- coding: utf-8 -*- 
# @Time : 2020/8/20 22:08 
# @Author : sml 
# @File : 41.和为S的两个数字.py 

"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res=[]
        min=float("inf")
        for i in range(len(array)):
            if tsum-array[i] in array[i+1:]:
                temp=array[i]*(tsum-array[i])
                if temp<min:
                    min=temp
                    res=[array[i],tsum-array[i]]
        return res





if __name__ == '__main__':
    f=Solution()
    array=[1,2,4,7,11,15]
    tsum=15
    print(f.FindNumbersWithSum(array,tsum))