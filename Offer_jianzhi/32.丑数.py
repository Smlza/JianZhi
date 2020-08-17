# -*- coding: utf-8 -*- 
# @Time : 2020/8/17 21:42 
# @Author : sml 
# @File : 32.丑数.py 

"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index:
            return -1
        array=[1]
        p0,p1,p2=0,0,0
        while len(array)<index:
            newnum=min(array[p0]*2,array[p1]*3,array[p2]*5)
            array.append(newnum)
            if newnum==array[p0]*2:
                p0+=1
            if newnum==array[p1]*3:
                p1+=1
            if newnum==array[p2]*5:
                p2+=1
        return array[-1]

if __name__ == '__main__':
    f=Solution()
    print(f.GetUglyNumber_Solution(4))
