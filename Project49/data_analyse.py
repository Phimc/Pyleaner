import pandas as pd
file_DF = None
a = 0
mod = 0
mean = 0
def load(filename):
    data = pd.read_csv(filename)
    global file_DF 
    file_DF = pd.DataFrame(data)
    return 0

def get_sum(Data,colomun):
    global a
    a = Data[colomun].sum()

def aver(Data,colomun):
    global mean
    meam = Data[colomun].mean()

def mode(Data,colomun):
    global mod
    mod = Data[colomun].mode()
    print(mod)
'''
file = load('test1.csv')
print(get_sum(file,'车辆总计'))
print(aver(file,'车辆总计'))
print(mode(file,'车辆总计'))
'''