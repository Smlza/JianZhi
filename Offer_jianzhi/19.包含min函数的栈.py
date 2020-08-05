# -*- coding: utf-8 -*- 
# @Time : 2020/8/5 20:42 
# @Author : sml 
# @File : 19.包含min函数的栈.py
"""题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
class Solution:
    def __init__(self):
        self.q = []
    def push(self, node):
        # write code here
        curMin = self.min()
        if curMin == None or node < curMin:
            curMin = node
        self.q.append((node, curMin))

    def pop(self):
        # write code here
        if len(self.q) == 0:
            return None
        else:
            return self.q.pop()

    def top(self):
        # write code here
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def min(self):
        # write code here
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]
