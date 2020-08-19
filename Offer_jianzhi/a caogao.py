# -*- coding: utf-8 -*- 
# @Time : 2020/8/13 18:38 
# @Author : sml 
# @File : a caogao.py 

# class Solution:
#     def match_str_in_sentence(self , s , x ):
#         # write code here
#         l=s.split(' ')
#         length=len(l)
#         for i in range(length):
#             if x in l[i]:
#                 return i+1
#         else:
#             return -1
# class Solution:
#     def daycost(self , len , m , n ):
#         # write code here
#         if m<=n:
#             return -1
#         if m>len:
#             return 1
#         if len<0 or m<0 or n<0:
#             return -1
#         else:
#             dayup= m-n
#             beforefinalday=(len-m)/dayup
#             if dayup==1:
#                 return int(beforefinalday)
#             if (len-m)%dayup!=0:
#                 beforefinalday+=1
#             return int(beforefinalday+1)
#
#
# if __name__ == '__main__':
#     len=10
#     m=4
#     n=3
#     f=Solution()
#     print(f.daycost(len,m,n))
# class Solution:
#     def sort(self , a , b ):
#         # write code here
#         l=[]
#         l.extend(a)
#         l.extend(b)
#         l.sort()
#         return l

#写一个装饰器
# def zhuangshi(func):
#     def f():
#         print("装饰头")
#         func()
#         print("装饰尾")
#     return f
#
# @zhuangshi #f1=zhuangshi(f1)
# def f1():
#     print("没有装饰")
#
# f1()

#写一个单例模式
# class Hero(object):
#     __instance=0
#     __isFirst=True
#
#     #创建一个单例对象，后面不在创建
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#         return cls.__instance
#     #只接受第一个对象的传值
#     def __init__(self,name,age):
#         if self.__isFirst:
#             self.name=name
#             self.age=age
#             Hero.__isFirst=False
#coding=utf-8
from multiprocessing import Pool
import os, time, random

def worker(msg):
    print("%s开始执行,进程号为%d"%(msg, os.getpid()))
    time.sleep(1)
    print("%s执行完毕"%(msg))

if __name__ == '__main__':
    po = Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(10):
        # Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))

    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")

