# -*- coding: utf-8 -*- 
# @Time : 2020/8/1 13:28 
# @Author : sml 
# @File : 2.替换空格.py 
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        count=len(s)
        for i in range(0,count):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)

