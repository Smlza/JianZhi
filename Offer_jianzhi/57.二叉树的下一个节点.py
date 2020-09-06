# -*- coding: utf-8 -*- 
# @Time : 2020/9/4 16:26 
# @Author : sml 
# @File : 57.二叉树的下一个节点.py 
"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

当该节点存在右子树时，那么下一个节点一定在右子树中产生
这种情况下又分成两种情况：
（1）右子树不存在左分支，那么要找的下一个节点就是右子树的根节点。
（2）右子树中存在左分支，那么不停的寻找左分支的左分支就可以了。
2.当该节点不存在右子树时，那么下一个节点一定在该节点的父节点中产生，这种情况下又分两种情况：
（1）该节点是他的父节点的左孩子，那么下一个节点就是该节点的父节点
（2） 该节点是他父节点的右孩子，那么就需要继续往该节点的父节点的父节点去寻找了。然后重复前面的分析。
"""
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):

        # write code here
        if pNode==None:
            return None
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode==pNode.next.left:
                    return pNode.next
                pNode=pNode.next
        return None


