# -*- coding: utf-8 -*- 
# @Time : 2020/9/6 16:34 
# @Author : sml 
# @File : 58.对称的二叉树.py

"""
题目描述
请实现一个函数，用来判断一棵二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.Symmetrical(pRoot.left,pRoot.right)
    def Symmetrical(self,left,right):
        if left==None and right==None:
            return True
        if left and right:
            return left.val==right.val and self.Symmetrical(left.left,right.right) and self.Symmetrical(left.right,right.left)

        return False





