# -*- coding: utf-8 -*- 
# @Time : 2020/8/7 22:08 
# @Author : sml 
# @File : 23.二叉树中和为某一值的路径.py 

"""
题目描述
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

思路：（1）首先该题是基于递归去遍历整棵树，遍历完每一条路径，遍历的顺序是先根节点，然后是左节点，接着是右节点；
（2）如果节点的左右子树都为空，且路径之和等于参数，就说明该路径是需要输出的
（3）如果不满足条件，在遍历完之后需要把最后一颗节点弹出来。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val==expectNumber:
            return [root.val]

        left=self.FindPath(root.left,expectNumber-root.val)
        right=self.FindPath(root.right,expectNumber-root.val)
        l=[]
        for i in (left+right):
            l.append([root.val]+i)

        return l

 # def find_path(tree, num):
 #    ret = []
 #    if not tree:
 #        return ret
 #    path = [tree]
 #    sums = [tree.val]
 #
 #    def dfs(tree):
 #        if tree.left:
 #            path.append(tree.left)
 #            sums.append(sums[-1]+tree.left.val)
 #            dfs(tree.left)
 #        if tree.right:
 #            path.append(tree.right)
 #            sums.append(sums[-1] + tree.right.val)
 #            dfs(tree.right)
 #        if not tree.left and not tree.right:
 #            if sums[-1] == num:
 #                ret.append([p.val for p in path])
 #        path.pop()
 #        sums.pop()
 #
 #    dfs(tree)
 #    return ret
