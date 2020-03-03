from tkinter import *


def callback():
    text_content.set('吹吧你我才不信呢')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

text_content = StringVar()
text_content.set('您所下载的影片含有未成年人限制内容，\n请满18周岁后点击')
textLable = Label(master=frame1, textvariable=text_content)
photo = PhotoImage(file='18.gif')
imgLable = Label(master=frame1, image=photo)
textLable.pack(side=TOP)
imgLable.pack(side=BOTTOM)

buttom = Button(frame2, text='我已满18周岁！', command=callback)
buttom.pack()

frame1.pack(padx=10, pady=20)
frame2.pack(padx=10, pady=20)


root.mainloop()
