# -*- coding: utf-8 -*- 
# @Time : 2020/8/19 21:36 
# @Author : sml 
# @File : 37.求二叉树的深度.py 
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot==None:
            return 0
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return max(left,right)+1

