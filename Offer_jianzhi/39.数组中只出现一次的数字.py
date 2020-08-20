# -*- coding: utf-8 -*- 
# @Time : 2020/8/19 22:02 
# @Author : sml 
# @File : 39.数组中只出现一次的数字.py 

"""
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here

        if not array:
            return []
        l=[]
        for i in array:
            if array.count(i)==1:
                l.append(i)
        return l


if __name__ == '__main__':
    f=Solution()
    array=[1,3,2,2,4,3,1,5]
    print(f.FindNumsAppearOnce(array))







