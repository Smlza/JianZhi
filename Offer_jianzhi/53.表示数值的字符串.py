# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 14:15 
# @Author : sml 
# @File : 53.表示数值的字符串.py 

"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 标记符号、小数点、e是否出现过
        sign = False
        decimal = False
        hasE = False
        for i in range(len(s)):
            if (s[i] == 'e' or s[i] == 'E'):
                # e后面一定要接数字
                if (i == len(s)-1):
                    return False
                # 不能同时存在两个e
                if (hasE == True):
                    return False
                hasE = True
            elif (s[i] == '+' or s[i] == '-'):
                # 第二次出现+-符号，则必须紧接在e之后
                if (sign and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                # 第一次出现+-符号，且不是在字符串开头，则也必须紧接在e之后
                elif (sign == False and i > 0 and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
                sign = True
            elif (s[i] == '.'):
                # e后面不能接小数点，小数点不能出现两次
                if (hasE or decimal):
                    return False
                decimal = True
            # 非法字符
            elif(s[i] < '0' or s[i] > '9'):
                return False
        return True

if __name__ == '__main__':
    f=Solution()
    print(f.isNumeric('.1'))