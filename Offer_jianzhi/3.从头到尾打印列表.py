# -*- coding: utf-8 -*- 
# @Time : 2020/8/1 13:29 
# @Author : sml 
# @File : 3.从头到尾打印列表.py 

#insert() 函数用于将指定对象插入列表的指定位置。

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l


