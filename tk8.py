from tkinter import *

root = Tk()


sb = Scrollbar(root)
sb.pack(side = RIGHT, fill = Y)

theLB = Listbox(root, yscrollcommand = sb.set)
theLB.pack()


for item in range(1000):
    theLB.insert(END, item)

sb.config(command=theLB.yview)

theBtn = Button(root, text='删掉它', command=lambda x = theLB: x.delete(ACTIVE))
theBtn.pack()


mainloop()
