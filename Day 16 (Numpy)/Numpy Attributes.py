'''
Hello Numpy :)
'''

import numpy as np

array = np.array([[1, 2, 3], [2, 3, 4]])  #列表转化为矩阵
print(array)

"""
Ouput:

array([1, 2, 3],
    [2, 3, 4])
"""

print("number of dim: ", array.ndim)  # 维度
# number of dim: 2

print("shape: ",array.shape)  # 行数和列数
# shape : (2, 3)

print("size: ",array.size)  # 元素个数
# size: 6