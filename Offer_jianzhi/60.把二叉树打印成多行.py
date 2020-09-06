# -*- coding: utf-8 -*- 
# @Time : 2020/9/6 19:37 
# @Author : sml 
# @File : 60.把二叉树打印成多行.py

"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        now,new=[pRoot],[]
        res_result=[]
        while now:
            res=[]
            for i in now:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
                res.append(i.val)
            res_result.append(res)
            now,new=new,[]
        return res_result

