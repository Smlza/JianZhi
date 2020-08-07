# -*- coding: utf-8 -*- 
# @Time : 2020/8/6 21:52 
# @Author : sml 
# @File : 21.从上往下打印二叉树.py

"""
思路：
（1）首先定义一个需要返回的列表 res
（2）每次遍历到有节点的时候都要插入节点值到res
（3）另外定义 nextlist 列表目的是保存下一层有节点的值
（4）等到下一层没有节点的时候，nextlist自然也就为空，跳出循环，返回res
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        newroot=[root]
        res=[]
        while newroot:
            newlist=[]
            for i in newroot:
                if i.left:
                    newlist.append(i.left)
                if i.right:
                    newlist.append(i.right)
                res.append(i.val)
            newroot=newlist

        return res






