"""
Radiobutton 选择按钮

摘要：
-使用 label_name.config() 可以改变lable里面的值：
    l.config(text='you have selected: ' + var.get())
-RadioButton 内部参数：
    window, text, variable, value, command 其中 variable 是当按钮被按下时，该参数名
    将被赋值成 value 指定的值
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', fg='black', width=20, text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected ' + var.get())  # config 是说把 l 里面的值给改变成另外一个值

ra1 = tk.Radiobutton(window, text='Option A',
        variable=var, value='A',  # 这段是当按钮按下时，var 将被赋值为 A
        command=print_selection)
ra1.pack()

ra2 = tk.Radiobutton(window, text='Option B',
        variable=var, value='B',
        command=print_selection)
ra2.pack()

ra3 = tk.Radiobutton(window, text='Option C',
        variable=var, value='C', 
        command=print_selection)
ra3.pack()

window.mainloop()