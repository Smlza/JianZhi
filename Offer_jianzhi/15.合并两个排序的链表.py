# -*- coding: utf-8 -*- 
# @Time : 2020/8/4 22:45 
# @Author : sml 
# @File : 15.合并两个排序的链表.py 

"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        Head=ListNode(0)
        p=Head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                Head.next=pHead1
                pHead1=pHead1.next
            else:
                Head.next=pHead2
                pHead2=pHead2.next
            Head=Head.next

        if pHead1:
            Head.next=pHead1
        elif pHead2:
            Head.next=pHead2
        return p.next



