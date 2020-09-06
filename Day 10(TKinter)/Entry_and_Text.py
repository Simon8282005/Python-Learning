import tkinter as tk

# 创建一个窗口
win = tk.Tk()
win.title("Entry and Text")
win.geometry('200x200')

# 创建一个entry
e = tk.Entry(win, show='*')
e.pack()


# 定义insert_point功能（在鼠标处添加文本）
def insert_point():
    var = e.get()
    t.insert('insert', var)  # insert('insert') = 在鼠标处添加文本


# 定义insert_end功能（在文本末端添加文本）
def insert_end():
    var = e.get()
    t.insert('end', var)  # insert('end') = 在文本末端添加文本
    # t.insert(1.1, var) = 在第一行的第一列添加文本


# Button （insert_point）
b1 = tk.Button(win, text='insert point', width=15,
               height=2, command=insert_point)
b1.pack()  # 把b1添加到窗口上

# Button（insert_end）
b2 = tk.Button(win, text='insert end',
               command=insert_end)
b2.pack()  # 把b2添加到窗口

# Text
t = tk.Text(win, height=2)
t.pack()

win.mainloop()
