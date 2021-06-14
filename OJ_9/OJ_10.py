# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:53:39 2021

@author: Phmc
"""
import pandas as pd
import numpy as np
import rainflow

file = pd.read_excel('rainflowdata.xlsx')
signal = file['Maximum [MPa]']
data = rainflow.extract_cycles(signal)
outfile = pd.DataFrame(data,columns=['rnh','mean','count','i_started','i_end'])
putfile = outfile.sort_values(by='mean')
putfile.to_excel('rainffffflow.xlsx')
