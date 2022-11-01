import numpy as np
a = np.random.randn(4, 3)  # a.shape = (4, 3)产生正态分布
b = np.random.randn(3, 2)  # b.shape = (3, 2)
c = np.dot(a,b)       ##不是矩阵乘法，只是对应下标相乘
print(c)