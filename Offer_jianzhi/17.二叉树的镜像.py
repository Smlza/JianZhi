# -*- coding: utf-8 -*-
# @Time : 2020/8/5 16:17
# @Author : turing
# @File : 17.二叉树的镜像.py

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param pRoot TreeNode类
# @return void
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if pRoot != None:
            pRoot.left,pRoot.right=pRoot.right,pRoot.left
            self.Mirror(pRoot.left)
            self.Mirror(pRoot.right)
        return pRoot