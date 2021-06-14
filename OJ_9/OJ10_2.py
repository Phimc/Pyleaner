from tkinter import *
import tkinter.messagebox as messagebox
top = Tk()
top.title('登录程序')
user_1 = StringVar()
pasw_1 = StringVar()
correct_username = '2077er'
correct_password = '2021610'
username_label = Label(top,text='Username:')
username_label.grid(row=1,column=1)
password_label = Label(top,text='password:')
password_label.grid(row=2,column=1)

username_text =  Entry(top)
username_text.grid(row=1,column=2)
password_text =  Entry(top,show='*')
password_text.grid(row=2,column=2)

Login_button = Button(top,text='Login',command=lambda:Login())
Login_button.grid(row=3,column=1)
Logout_button = Button(top,text='Logout',command=lambda:Logout())
Logout_button.grid(row=3,column=3)

def Login():
    user = str(username_text.get())
    pasw = str(password_text.get())
    if user == '':
        messagebox.showinfo('Wrong Username','Enter correct username,plz~')
    elif pasw == '':
        messagebox.showinfo('Wrong Password','Enter correct password,plz~')
    else:
        if (user == correct_username) and (pasw == correct_password):
            messagebox.showinfo('Successfully Login','尊敬的%s,您好！'%correct_username)
        else:
            if user != correct_username:
                messagebox.showinfo('Wrong Username','Enter correct username,plz~!')
            else:
                messagebox.showinfo('Wrong Password','Enter correct password,plz~')
def Logout():
    top.destroy()

top.mainloop()