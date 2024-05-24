# yyf_experiment2
import pandas as pd

# (1) 读取fifa19 数据集
df = pd.read_csv('fifa19/data.csv')

# 调用库计算'Dribbling'和'BallControl'的Pearson相关系数
correlation = df['Dribbling'].corr(df['BallControl'])

# 输出结果
print(f"The Pearson correlation between 'Dribbling' and 'BallControl' is {correlation}")

# 判断这两个属性的相关性
if correlation > 0:
    print("'Dribbling' and 'BallControl' are positively correlated.")
elif correlation < 0:
    print("'Dribbling' and 'BallControl' are negatively correlated.")
else:
    print("'Dribbling' and 'BallControl' have no correlation.")