# yyf_experiment2
import numpy as np
from scipy.interpolate import interp1d

# 创建自变量x
x = np.linspace(0, 10, num=11, endpoint=True)

# 创建因变量y1和y2
y1 = np.cos(-x**3/19.0)
y2 = np.sin(x**1.5/7.0)

# 创建线性插值函数
f1 = interp1d(x, y1, kind='linear')
f2 = interp1d(x, y2, kind='linear')

# 计算x为0.1、5、9时的y1和y2的值
x_new = [0.1, 5, 9]
y1_new = f1(x_new)
y2_new = f2(x_new)

# 输出结果
print(f"当x为{0.1}时，y1和y2的值分别为：{y1_new[0]}，{y2_new[0]}")
print(f"当x为{5}时，y1和y2的值分别为：{y1_new[1]}，{y2_new[1]}")
print(f"当x为{9}时，y1和y2的值分别为：{y1_new[2]}，{y2_new[2]}")