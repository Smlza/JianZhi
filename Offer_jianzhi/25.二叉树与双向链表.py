# -*- coding: utf-8 -*- 
# @Time : 2020/8/9 16:31 
# @Author : sml 
# @File : 25.二叉树与双向链表.py

"""题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。"""

"""
思路：中序遍历二叉搜索树存入列表，然后构造双向链表
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.mid=[]
        self.middle(pRootOfTree)
        for i in range(len(self.mid)-1):
            self.mid[i].right=self.mid[i+1]
            self.mid[i+1].left=self.mid[i]
        return self.mid[0]



    def middle(self,root):
        if not root:
            return
        self.middle(root.left)
        self.mid.append(root)
        self.middle(root.right)



