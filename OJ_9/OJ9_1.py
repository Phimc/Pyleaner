# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:50:10 2021

@author: Phmc
"""
import matplotlib.pyplot as plt
import numpy as np

x = [0,34,67,101,135,202,259,336,404,471]
y = [15.18,21.36,25.72,32.39,34.03,39.45,43.15,43.46,40.83,30.75]
call = np.polyfit(x,y,5)
x_a = np.linspace(0,471,1000)
y_a = np.polyval(call,x_a)
#绘图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('施肥量')
plt.ylabel('土豆产量')
plt.plot(x,y,label='原始曲线',marker='+',color='b')
plt.plot(x_a,y_a,label="拟合曲线",color = 'r')
plt.title('20377308 朱睦晨')
plt.plot(300,np.polyval(call,300),'o')
plt.annotate('(%d,%.2f)'%(300,np.polyval(call,300)), (300,np.polyval(call,300)))
plt.legend()
plt.show()