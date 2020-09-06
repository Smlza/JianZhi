# -*- coding: utf-8 -*- 
# @Time : 2020/9/6 19:15 
# @Author : sml 
# @File : 59.按之字形打印二叉树.py 

"""
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

思路：
对于每一行，一个列表存储结点用来遍历，一个列表存储节点的值，最后一个列表，通过设置flag来实现奇数行正序，偶数行逆序

"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        now,new=[pRoot],[]
        flag=0
        res_result=[]

        while now:
            res = []
            for i in now:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
                res.append(i.val)
            if flag==0:
                res_result.append(res)
                flag=1
            else:
                flag=0
                res_result.append(res[::-1])
            now,new=new,[]
        return res_result



