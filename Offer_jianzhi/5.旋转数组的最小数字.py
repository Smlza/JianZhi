# -*- coding: utf-8 -*- 
# @Time : 2020/8/1 15:21 
# @Author : sml 
# @File : 5.旋转数组的最小数字.py

"""把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。"""

# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here
#         if not rotateArray:
#             return 0
#         L=[]
#         for i in rotateArray:
#             L.append(i)
#         L.sort()
#         return L[0]

"""
0 0
LLRR

0 0
"""
# def f(local,ZL):
#     x=local[0]
#     y=local[1]
#     for i in ZL:
#         if i=='L':
#             x-=1
#         if i=='R':
#             x+=1
#         if i=='U':
#             y+=1
#         if i=='D':
#             y-=1
#     print(x,y)
#
#
# local=list(map(int,input().split(' ')))
# ZL=input()
# f(local,ZL)
"""
3 10 1000
100 5 3
50 3 2
300 3 3
"""
def f(m,wallet,shoplist):
    count=0
    weight=0
    price=0
    new_list=sorted(shoplist,key=lambda x: x[2],reverse=True)
    new1_list=sorted(new_list,key=lambda y: y[0])

    for i in range(len(new1_list)):


        if weight<=m and price<=wallet:
            count+=1
            weight += new1_list[i][1]
            price += new1_list[i][0]




    print(count-1)


num,m,wallet=list(map(int,input().split(' ')))
shoplist=[]
for i in range(num):
    shoplist.append(list(map(int,input().split(' '))))
f(m,wallet,shoplist)