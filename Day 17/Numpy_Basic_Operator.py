'''
Numpy基础运算
'''

import numpy as np

'''
一维矩阵运算
'''
a = np.array([10, 20, 30, 40])  # array([10, 20, 30, 40])
b = np.arange(4)  # array([0, 1, 2, 3])
c = a - b  # array([10, 19, 28, 37])
c2 = a + b  # array([10, 21, 32 43])
c3 = a * b  # array([0, 20, 60, 120])
c4 = b ** 2  # array([0, 1, 4, 9])
# sin = 三角函数
c5 = 10 * np.sin(a)  # array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])
# boolean
print(b < 3)  # array([ True,  True,  True, False], dtype=bool)

'''
多行多维度运算
'''

x = np.array([[1, 1],[0, 1]])
b = np.arange(4).reshape((2, 2))

print(a)  # array([[1, 1],
          #     [0, 1]])

print(b)  # array([[0, 1],
          #     [2, 3]])