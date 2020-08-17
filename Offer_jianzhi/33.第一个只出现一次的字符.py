# -*- coding: utf-8 -*- 
# @Time : 2020/8/17 22:25 
# @Author : sml 
# @File : 33.第一个只出现一次的字符.py

"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）.（从0开始计数）
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        a=[]
        for i in range(len(s)):
            if s.count(s[i])==1:
                a.append(i)
                return a[0]
        return -1






if __name__ == "__main__":
    print()

