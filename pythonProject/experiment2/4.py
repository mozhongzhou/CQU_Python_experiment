# yyf_experiment2
import pandas as pd

# (1) 读取fifa19 数据集
df = pd.read_csv('fifa19/data.csv')

# 显示数据的头部和尾部
print(df.head())
print(df.tail())

# (3) 筛选年龄在25 岁以下的年轻球员
young_players = df[df['Age'] < 25]

# 显示数据的头部和尾部
print(young_players.head())
print(young_players.tail())

# (4) 根据Jumping 分数对数据进行排序
sorted_players = young_players.sort_values(by='Jumping')

# 显示数据的头部和尾部
print(sorted_players.head())
print(sorted_players.tail())

# (5) 使用describe（）方法显示列Volleys 和Dribbling 的count、mean、std、min 和分位数数据
volleys_dribbling = df[['Volleys', 'Dribbling']].describe()

print(volleys_dribbling)