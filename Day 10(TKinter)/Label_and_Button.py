import tkinter as tk

# 创建一个窗口
window = tk.Tk()  # Tk 是一个object所以是大写
window.title("Hello Tkinter")
window.geometry('200x100')  # 设定窗口大小

var = tk.StringVar()
# Label也是一个object，所以也是大写
# Label(window) 意思是要在window窗口上创建一个label
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12),
             width=15, height=2)
l.pack()  # 放置label在window上

on_click = False


def hit_me():
    global on_click
    if not on_click:
        on_click = True
        var.set('you hit me')
    else:
        on_click = False
        var.set('')


# 按钮
b = tk.Button(window, text='hit me', width=15, height=2,
              command=hit_me)
b.pack()

window.mainloop()
