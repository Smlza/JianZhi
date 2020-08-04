# -*- coding: utf-8 -*- 
# @Time : 2020/8/4 22:38 
# @Author : sml 
# @File : 14.反转链表.py 

"""题目描述
输入一个链表，反转链表后，输出新链表的表头。

思路：
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        last=None
        while pHead:
            temp=pHead.next
            pHead.next=last
            last=pHead
            pHead=temp
        return last