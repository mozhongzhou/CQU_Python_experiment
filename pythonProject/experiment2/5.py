# yyf_experiment2
import pandas as pd

# (1) 读取fifa19 数据集
df = pd.read_csv('fifa19/data.csv')

# (2) 从数据中通过drop 删除以下三个属性Photo, Flag, Club Logo，显示结果；
df = df.drop(['Photo', 'Flag', 'Club Logo'], axis=1)
print(df.head())
print(df.tail())

# (3) 用isnull（）找出所有缺少值的条目；
missing_values = df.isnull().sum()
print(missing_values)

# (4) 用0 填补空值；
df = df.fillna(0)
print(df.head())
print(df.tail())

# (5) 将“Real Face”属性的特征值‘Yes’替换为1，‘No’变为0；“Preferred Foot”属性的特征值‘Right’变为1，‘Left’变为0, 并输出结果。
df['Real Face'] = df['Real Face'].map({'Yes': 1, 'No': 0})
df['Preferred Foot'] = df['Preferred Foot'].map({'Right': 1, 'Left': 0})
print(df.head())
print(df.tail())