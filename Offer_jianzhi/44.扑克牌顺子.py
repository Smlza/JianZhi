# -*- coding: utf-8 -*- 
# @Time : 2020/8/21 22:58 
# @Author : sml 
# @File : 44.扑克牌顺子.py 

"""
题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,
如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
 1.排序
 2.计算0的个数
 3.将除0之外剩余部分取出
 4.如果存在相等的元素，则不是顺子
 5.当非零数最大数-最小数-非零元素个数+1<0的个数
"""
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        num_sort=sorted(numbers)
        count=0
        for i in num_sort:
            if i==0:
                count+=1
            else:
                break
        num=num_sort[count:]
        n=len(num)
        for j in range(1,n):
            if num[j]==num[j-1]:
                return False
        if num[-1]-num[0]-n+1>count:
            return False

        return True



