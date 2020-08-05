# -*- coding: utf-8 -*-
# @Time : 2020/8/5 17:00
# @Author : turing
# @File : 18.顺时针打印矩阵.py
"""题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10."""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row=len(matrix)
        col=len(matrix[0])
        start=0 #层数
        l=[]
        while row>2*start and col>2*start:
            endx=row-1-start
            endy=col-1-start
            for i in range(start,endy+1):
                l.append(matrix[start][i])
            if endx>start:
                for i in range(start+1,endx+1):
                    l.append(matrix[i][endy])
            if endx>start and endy>start:
                for i in range(endy-1,start-1,-1):
                    l.append(matrix[endx][i])
            if endx-1>start and endy>start:
                for i in range(endx-1,start,-1):
                    l.append(matrix[i][start])
            start+=1
        return l
