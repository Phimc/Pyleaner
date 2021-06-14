# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:50:38 2021

@author: Phmc
"""
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-1,1,1000)
def f(x):
    return 1/(1+25*(x**2))

def f_lagrange(x, y, num_points, x_test):
    # 所有的基函数值，每个元素代表一个基函数的值
    q = np.zeros(shape=(num_points, ))

    # 计算第k个基函数的值
    for k in range(num_points):
        q[k] = 1
        # 计算第k个基函数中第k_个项（每一项：分子除以分母）
        for k_ in range(num_points):
            if k != k_:
                # 基函数
                q[k] = q[k]*(x_test-x[k_])/(x[k]-x[k_])
            else:
                pass 
    # 计算当前需要预测的x_test对应的y_test值        
    L = 0
    for i in range(num_points):
        L += y[i]*q[i]
    return L

x_5 = np.linspace(-1,1,5)
x_9 = np.linspace(-1,1,9)
x_13 = np.linspace(-1,1,13)
y_5 = [f(x) for x in x_5]
y_9 = [f(x) for x in x_9]
y_13 = [f(x) for x in x_13] 

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title('20377308 朱睦晨')
plt.ylim(-1.2,1.2)
Y = [f(x) for x in X]
plt.plot(X,Y,'-',label='f(x)',color='#000000') 
Y = [f_lagrange(x_5,y_5,5,x) for x in X] 
plt.plot(X,Y,'-.',label='n=4') 
Y = [f_lagrange(x_9,y_9,9,x) for x in X] 
plt.plot(X,Y,':',label='n=8') 
Y = [f_lagrange(x_13,y_13,13,x) for x in X] 
plt.plot(X,Y,'--',label='n=12') 
plt.legend()
plt.show()