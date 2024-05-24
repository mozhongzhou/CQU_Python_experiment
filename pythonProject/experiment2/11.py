import pandas as pd
import matplotlib.pyplot as plt

# 读取FIFA 19数据集
df = pd.read_csv('fifa19/data.csv')

# 绘制国家和球员数量的柱状图
df['Nationality'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Countries with Most Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.show()

# 绘制俱乐部和平均球员评分的柱状图
df.groupby('Club')['Overall'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('Top 10 Clubs with Highest Average Player Rating')
plt.xlabel('Club')
plt.ylabel('Average Player Rating')
plt.show()

# 绘制球员身高和体重的散点图

# 去掉身高和体重的缺失值
df = df.dropna(subset=['Height', 'Weight'])

# 将'Height'列的数据转换为厘米
df['Height'] = df['Height'].str.split("'").apply(lambda x: int(x[0])*12 + int(x[1])) * 2.54

# 将'Weight'列的数据转换为千克
df['Weight'] = df['Weight'].str.rstrip('lbs').astype(float) * 0.453592

# 绘制球员身高和体重的散点图
df.plot(kind='scatter', x='Height', y='Weight')
plt.title('Scatter plot of Player Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
