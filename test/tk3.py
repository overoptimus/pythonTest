import tkinter as tk


root = tk.Tk()

textLable = tk.Label(master=root, text='您所下载的影片含有未成年人限制内容，请满18周岁后点击')
photo = tk.PhotoImage(file='18.gif')
imgLable = tk.Label(master=root, image=photo)
textLable.pack(side=tk.TOP)
imgLable.pack(side=tk.BOTTOM)


root.mainloop()
