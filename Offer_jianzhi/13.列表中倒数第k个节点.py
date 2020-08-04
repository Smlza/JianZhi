# -*- coding: utf-8 -*- 
# @Time : 2020/8/3 20:19 
# @Author : sml 
# @File : 13.列表中倒数第k个节点.py 

"""题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""
#思路：Python 设置两个指针，p1，p2，先让p2走k-1步，然后再一起走，直到p2为最后一个 时，p1即为倒数第k个节点
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k<=0:
            return None
        p1=head
        p2=head
        while k-1>0:
            if p2.next!=None:
                p2=p2.next
                k-=1
            else:
                return None
        while p2.next!=None:
            p1=p1.next
            p2=p2.next
        return p1



