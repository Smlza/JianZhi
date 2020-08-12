# -*- coding: utf-8 -*- 
# @Time : 2020/8/9 14:46 
# @Author : sml 
# @File : 24.复杂链表的复制.py
"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

"""
思路：1 复制原来的链表，顺次连接形成新链表
      2 利用原节点的random指向，来用复制的相应节点的random
      3 将复制好的链表拆分出来，或者说将 偶数位的节点重新拆分合成新的链表，得到的就是复制的链表
"""
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
    #1 复制原来的链表，顺次连接形成新链表
        CloneNode=pHead
        while CloneNode:
            node=RandomListNode(CloneNode.label)
            node.next=CloneNode.next
            CloneNode.next=node
            CloneNode=node.next
    #2 利用原节点的random指向，来用复制的相应节点的random
        CloneNode=pHead
        while CloneNode:
            node=CloneNode.next #指向复制的节点
            if CloneNode.random:
                node.random=CloneNode.random.next #经过第一步，复制的节点都在原节点的下一个，所以这边指向随机节点的下一个
            CloneNode=node.next  #下一次循环开始
        CloneNode=pHead
        pHead=pHead.next
        while CloneNode.next:
            node=CloneNode.next
            CloneNode.next=node.next
            CloneNode=node
        return pHead



