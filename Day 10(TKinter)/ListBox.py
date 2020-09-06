"""
ListBox (选项表)
"""

import tkinter as tk

win = tk.Tk()
win.title("Entry and Text")
win.geometry('200x200')

# var1, 在window上方显示选择物体的变量
var1 = tk.StringVar()
lable = tk.Label(win, bg='white', width=4, textvariable=var1)
lable.pack()


# 打印出鼠标选择的物体
def print_selection():
    value = lb.get(lb.curselection())  # curselection = cursor selection （鼠标选择）
    var1.set(value)


b1 = tk.Button(win, text='print selection', width=15,
               height=2, command=print_selection)
b1.pack()

# 显示在list_box上的物体
var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(win, listvariable=var2)  # list_box的显示物体的值的名是listvariable，textvariable是给text用的
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

win.mainloop()
