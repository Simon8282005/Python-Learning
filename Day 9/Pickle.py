'''
pickle模块可是存放上一次的运行结果，以便下一次可以比较方便的去修改

'''

import pickle

a_dict = {'da': 1, 2: [23, 1, 2], '100': [111]}

#file = open('picke_example.pickle','wb')
#pickle.dump(a_dict, file)
#file.close()

# 第一种写法
file = open('picke_example.pickle', 'rb')
a_dict1 = pickle.load(file)
file.close()

# 另外一种比较简单的写法,不用担心忘记关掉file，因为
# with语句执行完之后会自动关闭
with open('picke_example.pickle', 'rb') as file:
    a_dict1 = pickle.load(file)

print(a_dict1)
