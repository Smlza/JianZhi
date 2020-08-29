# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 10:25 
# @Author : sml 
# @File : 49.把字符串转换成函数.py 
"""
题目描述
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

思路：1.先考虑第一个字符是否存在[+,-]
    2.考虑字符串内是否有特殊字符，有就返回0
    3.考虑字符串是否仅有[+,-]
    4.考虑空字符串
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        dic1={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        dic2={"+":1,"-":-1}
        if not s or len(s)<1:
            return 0
        first=s[0]
        if first in ["+","-"]:
            flag=dic2[first]
            if len(s)==1:
                return 0
            x=0
            for i in s[1:]:
                if i not in dic1:
                    return 0
                x=x*10+dic1[i]
            return flag*x
        else:
            x=0
            for i in s[0:]:
                if i not in dic1:
                    return 0
                x=x*10+dic1[i]
            return x

if __name__ == '__main__':
    f=Solution()
    print(f.StrToInt("+123"))