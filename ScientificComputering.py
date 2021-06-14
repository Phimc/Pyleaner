# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:02:04 2021

@author: Phmc
"""
import numpy as np
import matplotlib.pyplot as plt
k = np.random.randn(5000)
plt.subplot(221)
plt.hist(k,bins=20,density=True)

plt.subplot(222)
plt.hist(k,bins=40,density=True)

plt.subplot(223)
plt.hist(k,bins=80,density=True)

plt.subplot(224)
plt.hist(k,bins=160,density=True)

plt.show()