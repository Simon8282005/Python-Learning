import tkinter as tk
import tkinter.messagebox as tkbox
import pickle

# main windows
win = tk.Tk()
win.title('Login Screen')
win.geometry('450x300')

# welcome image
canvas = tk.Canvas(win, height=500, width=500)  # 创建画布
image_file = tk.PhotoImage(file='welcome.gif')  # 加载图片文件
image = canvas.create_image(0,0,anchor='nw', image=image_file)  # 将图片置于画布上
canvas.pack(side='top')  # 放置画布（为上端）

# user information
tk.Label(win, text='用户名: ').place(x = 50, y = 150)
tk.Label(win, text='密码： ').place(x = 50, y = 190)

var_usr_name = tk.StringVar()
var_usr_name.set('Simon@python.com')
entry_usr_name = tk.Entry(win, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(win, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x = 160, y = 190)

def usr_login():
    ##这两行代码就是获取用户输入的`usr_name`和`usr_pwd`
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    
    ##这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    ##中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        ##这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
        ##的用户和密码写入，即用户名为`admin`密码为`admin`。
            with open('usrs_info.pickle','wb') as usr_file:
                usrs_info = {'admin':'admin'}
                pickle.dump(usrs_info, usr_file)
    #如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗`how are you?`加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcom', message='How are you ?' + usr_name)
        ##如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tk.messagebox.showerror(message='Error, your passward is wrong, try again. ')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome','You have not sign up yet. Sign up today ?')

        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_Mofan_Python():
        ##以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        ##这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)

        ##这里就是判断，如果两次密码输入不一致，则提示`'Error', 'Password and confirm password must be the same!'`
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')

        ##如果用户名已经在我们的数据文件中，则提示`'Error', 'The user has already signed up!'`
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')

        ##最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功`'Welcome', 'You have successfully signed up!'`
        ##然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            ##然后销毁窗口。
            window_sign_up.destroy()
    
    window_sign_up = tk.Toplevel(win)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()#将输入的注册名赋值给变量
    new_name.set('example@python.com')#将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)#将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)#创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=150, y=10)#`entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    # 下面的 sign_to_Mofan_Python 我们再后面接着说
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(win, text='Login', command=usr_login)
btn_login.place(x = 170, y = 230)
btn_sign_up = tk.Button(win, text='Sign Up', command=usr_sign_up)
btn_sign_up.place(x = 270, y = 230)

win.mainloop()