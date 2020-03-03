from tkinter import *

root = Tk()

girls = ['西施', '貂蝉', '杨玉环', '王昭君']

v = IntVar()
i = 1

for girl in girls:
    b = Radiobutton(root, text = girl, variable = v, value = i)
    b.pack(anchor=W)
    i += 1

label = Label(root, textvariable = v)
label.pack()







# v = IntVar()
#
# c = Checkbutton(root, text='测试一下', variable=v)
# c.pack()
#
# l = Label(root, textvariable = v)
# l.pack()

root.mainloop()
