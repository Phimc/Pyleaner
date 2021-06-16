import tkinter as tk

from numpy import left_shift, string_
import data_analyse as dt

top = tk.Tk()
top.title('Data analyse')
top.geometry('500x300')
# 绘制菜单
menubar = tk.Menu(top)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='Open', command=dt.load('test1.csv'))
filemenu.add_command(label='Save', command=None)
filemenu.add_command(label='Exit',command=top.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='Sum', command=lambda:dt.get_sum(dt.file_DF,'车辆总计'))
editmenu.add_command(label='Mean', command=lambda:dt.aver(dt.file_DF,'车辆总计'))
editmenu.add_command(label='Mode', command=lambda:dt.mode(dt.file_DF,'车辆总计'))

top.config(menu=menubar)

fn = tk.StringVar()


top.mainloop()
