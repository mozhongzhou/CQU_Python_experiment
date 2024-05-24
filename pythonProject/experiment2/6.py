# yyf_experiment2
import pandas as pd
import matplotlib.pyplot as plt
# (1) 读取fifa19 数据集
df = pd.read_csv('fifa19/data.csv')
# 定义最大-最小规范化函数
def min_max_normalization(df, column_name):
    min_value = df[column_name].min()
    max_value = df[column_name].max()
    df[column_name] = (df[column_name] - min_value) / (max_value - min_value)
    return df

# 对列Age 进行最大-最小化处理
df = min_max_normalization(df, 'Age')

# 输出结果
print(df['Age'])

# 用直方图显示
plt.hist(df['Age'], bins=30, alpha=0.5, color='g')
plt.xlabel('Normalized Age')
plt.ylabel('Frequency')
plt.title('Histogram of Normalized Age')
plt.grid(True)
plt.show()