a_list = [1, 2, 3, 4, 5, 6]  # 列表

'''
语法
'value_name': key
key可以是数字或字符(String)

'''
d = {'apple': 1, 'pear': 2, 'orange': 3}  # 字典
d2 = {1: 'a', 'b': 'c'}

d3 = {'apple': [1, 2, 3], 'pear': {1: 3, 3: 'a'}, 'orange': 8}  # function:name}  # 也可以这样写 :)
print(d3['pear'][3])


print(d['apple'])  # 打印字典
print(a_list[0])  # 打印列表

del d['pear']  # 把字典里的pear元素删了
print(d)

d['b'] = 20  # 添加'b'到字典里，'b'的值是20
print(d)
