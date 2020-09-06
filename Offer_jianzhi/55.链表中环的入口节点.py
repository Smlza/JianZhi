# -*- coding: utf-8 -*- 
# @Time : 2020/8/25 15:33 
# @Author : sml 
# @File : 55.链表中环的入口节点.py 

"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""



# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead ==None or pHead.next==None:
            return None
        p=pHead
        l=[]
        while p:
            if p in l:
                return p
            else:
                l.append(p)
                p=p.next
        return None




