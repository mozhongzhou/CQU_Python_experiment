import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取fifa19 数据集
df = pd.read_csv('fifa19/data.csv')

# 获取'Dribbling'和'BallControl'列
dribbling = df['Dribbling']
ball_control = df['BallControl']

# 计算平均值
mean_dribbling = np.mean(dribbling)
mean_ball_control = np.mean(ball_control)

# 计算分子
numerator = np.sum((dribbling - mean_dribbling) * (ball_control - mean_ball_control))

# 计算分母
denominator = np.sqrt(np.sum((dribbling - mean_dribbling)**2) * np.sum((ball_control - mean_ball_control)**2))

# 手动计算Pearson相关系数
correlation_manual = numerator / denominator

# 使用pandas库的corr方法计算Pearson相关系数
correlation_pandas = df['Dribbling'].corr(df['BallControl'])

# 比较两种方法的结果
if np.isclose(correlation_manual, correlation_pandas):
    print("The results are consistent.")
else:
    print("The results are not consistent.")

# 绘制散点图
plt.scatter(df['Dribbling'], df['BallControl'])

# 设置标题和坐标轴标签
plt.title('Scatter plot of Dribbling vs BallControl')
plt.xlabel('Dribbling')
plt.ylabel('BallControl')

# 显示图形
plt.show()