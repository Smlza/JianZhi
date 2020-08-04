# -*- coding: utf-8 -*- 
# @Time : 2020/8/4 23:05 
# @Author : sml 
# @File : 16.树的子结构.py 

"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result=False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result=self.issame(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result

    def issame(self,p1,p2):
        if not p2:
            return True
        if not p1:
            return False
        return p1.val==p2.val and self.issame(p1.left,p2.left) and self.issame(p1.right,p2.right)
