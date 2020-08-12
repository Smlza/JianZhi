# -*- coding: utf-8 -*- 
# @Time : 2020/8/12 22:00 
# @Author : sml 
# @File : 26.字符串排列.py 
"""题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入：输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""
class Solution:
    def Permutation(self, ss):
        # write code here
        length=len(ss)
        if length <= 1:
            return ss
        list1=[]
        for i in range(length):
            first_str=ss[i]
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                temp= first_str + j
                if temp not in list1:
                    list1.append(temp)
        list1.sort()

        return list1

