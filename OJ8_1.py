# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:59:44 2021
大计基OJ8-1
@author: Phmc
"""

import numpy as np
import matplotlib.pyplot as plt
def taylorsin(k,x):
    y=0
    for i in range(0,k+1):
        #自定义泰勒展开式和项
        y=((-1)**i)*(x**(2*i+1))/np.math.factorial(2*i+1)+y
    return y
X = np.linspace(-3*np.pi/2,3*np.pi/2,2000)
f=np.sin(X)
g=[taylorsin(2,i) for i in X]
plt.plot(X,f,label='sinx',color='b')
plt.plot(X,g,label='taylor curve',color='r')
plt.plot(-np.pi/2,np.sin(-np.pi/2),color='b',marker='o')
plt.plot(np.pi/2,np.sin(np.pi/2),color='b',marker='o')
plt.annotate('($-\pi$/2,-1)',((-np.pi/2,np.sin(-np.pi/2))),color='b')
plt.annotate('($\pi$/2,1)',((np.pi/2,np.sin(np.pi/2))),color='b')
plt.xticks([-np.pi*3/2,-np.pi*3/4,0,np.pi*3/4,np.pi*3/2])
plt.legend()
plt.show()
