# -*- coding: utf-8 -*- 
# @Time : 2020/8/18 22:18 
# @Author : sml 
# @File : 35.两链表的第一个公共节点.py 

"""题目描述
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，
所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
用栈的思想，从尾部开始找到公共节点
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        stack1=[]
        stack2=[]
        while pHead1:
            stack1.append(pHead1)
            pHead1=pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2=pHead2.next
        pre=None
        while stack1 and stack2 and stack1[-1]==stack2[-1]:
            pre=stack1.pop()
            stack2.pop()
        return pre
