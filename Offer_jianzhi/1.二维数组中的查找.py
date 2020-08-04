# -*- coding: utf-8 -*- 
# @Time : 2020/8/1 13:24 
# @Author : sml 
# @File : 1.二维数组中的查找.py 

class Solution:
    # array 二维列表
    def Find(self, target, array):

        # -*- coding:utf-8 -*
        # write code here
        flag = 'false'
        height = len(array)
        for h in range(height):
            if target in array[h]:
                flag = "true"
                break
        return flag


while True:
    try:
        S = Solution()
        # 字符串转为list
        L = list(eval(raw_input()))
        array = L[1]
        target = L[0]
        print(S.Find(target, array))
    except:
        break

