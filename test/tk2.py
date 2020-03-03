import tkinter as tk

class App:
    def __init__(self, master):
        frame = tk.Frame(master=master)
        frame.pack(side = tk.BOTTOM)

        self.hi_there = tk.Button(master=frame, text = '打招呼', fg = 'blue', command = self._say_hi)
        self.hi_there.pack()

    def _say_hi(self):
        print('互联网的广大朋友们好，我是常江！')

root = tk.Tk()
app = App(root)

root.mainloop()
