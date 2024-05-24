# yyf_experiment1
import numpy as np

# 创建一个10x10的数组，所有元素都是0
zeros = np.zeros((10, 10))

# 创建一个10x10的单位矩阵
identity = np.eye(10)

# 创建一个10x10的数组，所有元素都是在[0,100]范围内随机生成的整数
randoms = np.random.randint(0, 101, size=(10, 10))

# 输出所有数组
print('Zeros:\n', zeros)
print('Identity:\n', identity)
print('Randoms:\n', randoms)