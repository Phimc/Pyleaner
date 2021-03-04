# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:32:27 2021

@author: Phmc
"""
class Stack():
    def __init__(self):
        self.items = [] #空栈初始化（空数组）
        
    def push(self,items):
        self.items.append(items)
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

s = input() #输入str
numst = Stack() #数字栈
cacu = Stack() #运算符号栈
sign = [] #运算符号list
#生成运算符号list
st = list(s)
for i in range(len(s)):
    if s[i] == '+' or s[i] == '*':
        sign.append(s[i])
        st[i] = ' '
stc = ''.join(st)
num = list(map(int,stc.split(' '))) #数字list
#第一个数字入栈
numst.push(num[0])
for i in range(len(sign)):
    #逐个读取数字i+1，符号i
    if sign[i] == '*':#如果是*，pop出栈顶与新数字做乘法
        n1 = numst.peek()
        numst.pop()
        numst.push((n1 % 10000)*(num[i+1]%10000))
    elif sign[i] == '+': 
        if cacu.isEmpty():
            numst.push(num[i+1])
            cacu.push(sign[i])
        elif cacu.peek() == '*':
            n1 = numst.peek()
            numst.pop()
            n2 = numst.peek()
            numst.pop()
            numst.push((n1 % 10000)*(n2 % 10000))
        else:
            n1 = numst.peek()
            numst.pop()
            n2 = numst.peek()
            numst.pop()
            numst.push((n1 % 10000)+(n2 % 10000))
            numst.push(num[i+1])
            cacu.push(sign[i])
            
sumnum = 0
#求和
while not numst.isEmpty():
    sumnum += numst.peek()
    sumnum % 10000
    numst.pop()
print(sumnum % 10000)