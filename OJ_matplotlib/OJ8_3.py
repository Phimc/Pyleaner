# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:30:40 2021
大计基OJ8-3
@author: Phmc
"""

import numpy as np
import matplotlib.pyplot as plt
s = list(input())
dic = {}
# 统计字频
for char in s:
    try:
        dic[char] += 1
    except :
        dic[char] = 1
# 降序排列
group = sorted(dic.items(),key = lambda kv:(kv[1],kv[0]))        
group.reverse()
characters = [point[0]for point in group]
char_times = [point[1]for point in group]

x = np.arange(len(characters))
width = 0.5
colorv = np.linspace(0,0.5,len(characters))
colorset = [0 for i in range(len(characters))]
for i in range(len(colorset)):
    colorset[i] =plt.cm.Spectral(colorv[i])
fg = plt.figure(figsize=(4.8, 3.6))
ax = plt.axes()
ct = ax.bar(x,char_times,width,color=colorset)
ax.set_title('Input:%s'%''.join(s))
ax.set_ylabel('Counts')
ax.set_xlabel('Character(s)')
ax.set_xticks(x)
ax.set_xticklabels(characters)

#fg.tight_layout()
fg.savefig('hwjj.png',dpi=300)
plt.show()
