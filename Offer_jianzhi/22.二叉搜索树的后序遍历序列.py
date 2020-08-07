# -*- coding: utf-8 -*- 
# @Time : 2020/8/6 22:22 
# @Author : sml 
# @File : 22.二叉搜索树的后序遍历序列.py 

"""题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：二叉搜索树的中序遍历是个递增序列，可以看成中序遍历和后续遍历是否为同一棵二叉树
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code
        length=len(sequence)
        if length==0:
            return False
        if length==1:
            return True
        root=sequence[-1]
        left=0
        while sequence[left] < root:
            left+=1
        for i in range(left,length-1):
            if sequence[i]< root:
                return False
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])
