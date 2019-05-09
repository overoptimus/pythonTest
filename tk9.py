from tkinter import *

root = Tk()

text = Text(root, width = 40, height = 30)
text.pack()

text.insert(INSERT, 'l love ')
text.insert(END, 'you')
img = PhotoImage(file='18.gif')

def show():
    print('我被点了。。。')
    text.image_create(END, image = img)


btn = Button(text, text = '点我', command = show)
text.window_create(INSERT, window=btn)

mainloop()
