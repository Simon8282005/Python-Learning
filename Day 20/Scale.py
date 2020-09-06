import tkinter as tk

"""
scale_name = tk.Scale(window, label='try me', from_=5, to=11, 
    orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, 
    resolution=0.01, command=print_selection)

-参数from_=5，to=11的意思就是从5到11，即这个滚动条最小值为5，最大值为11
 （这里使用from_是因为在python中有from这个关键词）
-参数orient=tk.HORIZONTAL在这里就是设置滚动条的方向，如我们所看到的效果图，
 这里HORIZONTAL就是横向。
-参数length这里是指滚动条部件的长度，但注意的是和其他部件width表示不同，width表示的是以字符为单位，
 比如width=4，就是4个字符的长度，而此处的length=200，是指我们常用的像素为单位，即长度为200个像素
-参数resolution=0.01这里我们可以借助数学题来理解，我们做的很多数学题都会让我们来保留几位小数，
 此处的0.01就是保留2位小数，即效果图中的5.00 9.00等等后面的两位小数， 
 如果保留一位就是resolution=0.1 这里的showvalue就是设置在滚动条上方的显示。
 showvalue=0显示的就是效果图，上方无结果显示
-参数tickinterval设置的就是坐标的间隔，此处为tickinterval=2，
 显示的即为效果图中的5.00 7.00 9.00 11.00 
 如果改为tickinterval=3则为5.00 8.00 11.00
"""

window = tk.Tk()
window.title('Scale')
window.geometry('200x200')

var = tk.StringVar()

def print_selection(v):
    l1.config(text='you have selected' + v)

s1 = tk.Scale(window, label='try me', from_=5, to=11, 
    orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, 
    resolution=0.01, command=print_selection)
s1.pack()

l1 = tk.Label(window, bg='yellow', fg='black', font=('Ubuntu Mono', 12), text=' ')
l1.pack()

window.mainloop()