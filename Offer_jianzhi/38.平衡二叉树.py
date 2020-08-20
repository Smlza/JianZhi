# -*- coding: utf-8 -*- 
# @Time : 2020/8/19 21:51 
# @Author : sml 
# @File : 38.平衡二叉树.py 

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot==None:
            return True
        if abs(self.Tree_depth(pRoot.left)-self.Tree_depth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def Tree_depth(self,pRoot):
        if pRoot==None:
            return 0
        left=self.Tree_depth(pRoot.left)
        right=self.Tree_depth(pRoot.right)
        return max(left,right)+1

