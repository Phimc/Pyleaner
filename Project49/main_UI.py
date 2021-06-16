import tkinter as tk

from numpy import left_shift, string_
import data_analyse as dt
filename='test1.csv'
top = tk.Tk()
top.title('Data analyse')
top.geometry('500x300')
# 绘制菜单
details = tk.StringVar()
detail_Lable = tk.Label(top,textvariable=details)
detailstr=['请选择文件']
details.set(''.join(detailstr))
def choosefile(filename):
    dt.load(filename)
    detailstr=['已选择文件 '+str(filename)+'\n']
    details.set(''.join(detailstr))

def choosefilefrom():
    chosen_file = str(list(filetext.get(1.0)))
    dt.load(chosen_file)
    detailstr=['已选择文件 '+str(chosen_file)+'\n']
    details.set(''.join(detailstr))
detail_Lable.pack()

filetext = tk.Text(top)
filetext.pack()



menubar = tk.Menu(top)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='Open', command=lambda:choosefile(filename))
filemenu.add_command(label='OpenCsv', command=lambda:choosefilefrom())
filemenu.add_command(label='Exit',command=top.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='Sum', command=lambda:dt.get_sum(dt.file_DF,'车辆总计'))
editmenu.add_command(label='Mean', command=lambda:dt.aver(dt.file_DF,'车辆总计'))
editmenu.add_command(label='Mode', command=lambda:dt.mode(dt.file_DF,'车辆总计'))

top.config(menu=menubar)



top.mainloop()
