from tkinter import *


def check():
    print('account:', v1.get())
    print('password:', v2.get())

def onclick():
    account.delete(0)
    password.delete(0)

root = Tk()

v1 = StringVar()
v2 = StringVar()
label1 = Label(root, text = '账号：')
lable2 = Label(root, text = '密码：')
label1.grid(row = 0, column = 0)
lable2.grid(row = 1, column = 0)
account = Entry(root, textvariable = v1)
password = Entry(root, textvariable = v2, show = '*')
account.grid(row = 0, column = 1)
password.grid(row = 1, column = 1)

btn_check = Button(root, text = '获取信息', command = check)
btn_trust = Button(root, text ='清空', command = onclick)
btn_check.grid(row = 2, column = 0, sticky = W, padx = 20)
btn_trust.grid(row = 2, column = 1, sticky = E, padx = 20)

mainloop()
