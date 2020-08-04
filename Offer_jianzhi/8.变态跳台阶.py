# -*- coding: utf-8 -*- 
# @Time : 2020/8/2 12:45 
# @Author : sml 
# @File : 8.变态跳台阶.py

"""题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。"""


class Solution:
    def jumpFloorII(self, number):
        if number==1 :
            return 1
        else:
            return pow(2,number-1)





# if __name__ == "__main__":
#     print()

