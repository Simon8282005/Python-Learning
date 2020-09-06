import copy

a = [1, 2, 3]
b = a  # a 和 b 是一样的,a 被改变的话 b 也是被改变
print(id(a))

'''
浅复制
'''

c = copy.copy(a)  # 运用copy模块
print(id(c))

c[1] = 222222
print("This is c after modifited: ", c)
print("This is a: ", a)
'''
This is c after modifited:  [1, 222222, 3]
This is a:  [1, 2, 3]
'''

a = [1, 2, [3, 4]]
d = copy.copy(a)
print(id(a) == id(b))  # Output: False
print(id(a[1]) == id(b[1]))  # Output: True

'''
深复刻
'''

# 所以要将第二个列表也复制的话叫深复刻（deepcopy）
# deepcopy让两个列表的id完全不一样 (众：都讲两个不一样的东西咯！)
e = copy.deepcopy(a)
print("\nDeepcopy\n", "Id e isn't = a ?: ", id(e[1]) == id(a[2]))
# Output = False

'''
结论：
    copy = 第一层列表被copy到不一样到内存空间，但第二层的不会
    deepcopy = 全部的列表都别copy到不一样到的内存空间去了
'''
