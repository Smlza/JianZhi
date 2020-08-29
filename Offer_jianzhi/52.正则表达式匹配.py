# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 12:46 
# @Author : sml 
# @File : 52.正则表达式匹配.py 
"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

思路：当模式中的第二个字符是“*”时：
如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
1.模式后移2字符，相当于x*被忽略；
2.字符串后移1字符，模式后移2字符，相当于x*匹配一位；
3.字符串后移1字符，模式不变，即继续匹配字符下一位，相当于x*匹配多位；
当模式中的第二个字符不是“*”时：
如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的部分。
如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回False。
"""
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        if len(s)>0 and len(pattern)==0:
            return False
        if len(pattern)>1 and pattern[1]=='*':
            if s and (pattern[0]=='.' or pattern[0]==s[0]):
                f1=self.match(s,pattern[2:]) #* 匹配0个字符
                f2=self.match(s[1:],pattern[2:]) #* 匹配1个字符
                f3=self.match(s[1:],pattern) #*匹配多个字符
                if f1 or f2 or f3:
                    return True
                else:
                    return False
            else:
                return self.match(s,pattern[2:]) #s为空串，*匹配0个字符时
        elif  s and (pattern[0]=='.' or pattern[0]==s[0]):
            return self.match(s[1:],pattern[1:])
        else:
            return False



