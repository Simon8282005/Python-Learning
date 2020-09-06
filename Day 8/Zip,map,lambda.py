"""
zip
"""
a = [1, 2, 3]
b = [4, 5, 6]
zip(a, b)  # 把a和b给zip起来
print(list(zip(a, b)))  # 把zip可视化
# Output = [(1,4),(2,5),(3,6)]

for i, j in zip(a, b):
    print(i / 2, j * 2)
    # 结果：
    # 0.5 8
    # 1.0 10
    # 1.5 12

'''
lambda
'''


def fun1(x, y):
    return x + y


print("\nThis is def: ", fun1(1, 2))

fun2 = lambda x, y: x + y
print("This is lambda: ", fun2(1, 2))

'''
map
'''

# 用fun1来同时运算两个数字
print("This is map: ", list(map(fun1, [1, 3], [2, 5])))
# Output[3,8]

