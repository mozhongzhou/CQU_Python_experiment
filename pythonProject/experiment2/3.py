# yyf_experiment2
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 创建x的值
x = np.linspace(0, 2 * np.pi, 100)

# 计算y1和y2的值
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个新的图形，并设置其大小
plt.figure(figsize=(12, 5))

# 绘制y1和y2的图形
plt.plot(x, y1, color='red', linewidth=2, label='y1=sinx')
plt.plot(x, y2, color='blue', linewidth=2, label='y2=cosx')

# 设置标题，x轴和y轴的标签，以及图例
plt.title('sinx 与 cosx')
plt.xlabel('x值')
plt.ylabel('y值')
plt.legend()

# 显示图形
plt.show()