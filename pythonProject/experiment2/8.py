# yyf_experiment2
import pandas as pd

import numpy as np
# (1) 读取fifa19 数据集
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

# 计算Pearson相关系数
correlation = numerator / denominator

# 输出结果
print(f"The Pearson correlation between 'Dribbling' and 'BallControl' is {correlation}")

# 判断这两个属性的相关性
if correlation > 0:
    print("'Dribbling' and 'BallControl' are positively correlated.")
elif correlation < 0:
    print("'Dribbling' and 'BallControl' are negatively correlated.")
else:
    print("'Dribbling' and 'BallControl' have no correlation.")