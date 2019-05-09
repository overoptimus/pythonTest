from tkinter import *

root = Tk()

group = LabelFrame(root, text='最好的脚本语言是？', padx=5, pady=5)
group.pack(padx=5, pady=5)

languages = [
    ('Python', 1),
    ('Perl', 2),
    ('Ruby', 3),
    ('Lua', 4)
]

v = IntVar()
v.set(1)

for (lang, num) in languages:
    b = Radiobutton(group, text = lang, variable = v, value = num, indicatoron=FALSE)
    # b.pack(anchor=W)
    b.pack(fill=X)

mainloop()
