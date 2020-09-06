# -*- coding: utf-8 -*- 
# @Time : 2020/9/4 15:36 
# @Author : sml 
# @File : 56.删除链表中重复的节点.py
"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
 1 设置一个new_head指向原表头
 2 两个指针，一个cur去找重复的，直到不重复的节点，pre.next指向cur
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead==None:
            return
        if pHead.next==None:
            return pHead
        new_head=ListNode(-1)
        new_head.next=pHead   #设置一个new_head指向原表头
        pre,cur=None,new_head
        while cur:
            pre=cur
            cur=cur.next
            while cur and cur.next and cur.val==cur.next.val: #找开始重复
                t=cur.val
                while cur and t==cur.val:
                    cur=cur.next
                pre.next=cur
        return new_head.next



