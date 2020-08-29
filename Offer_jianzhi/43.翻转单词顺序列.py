# -*- coding: utf-8 -*- 
# @Time : 2020/8/21 22:31 
# @Author : sml 
# @File : 43.翻转单词顺序列.py 
"""
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""
# s='I am a student'
# print(s.split(' '))
class Solution:
    def ReverseSentence(self, s):
        # write code here
        l=s.split(' ')
        s_new=[]

        for i in range(len(l)):
            s=l[-1]
            l.pop()
            s_new.append(s)
        str_new=' '.join(s_new)


        return str_new

if __name__ == '__main__':
    f=Solution()
    s="student. a am I"

    print(f.ReverseSentence(s))