# yyf_experiment2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# (1) 读取fifa19 数据集
df = pd.read_csv('fifa19/data.csv')

# 定义z-score 规范化函数
def z_score_normalization(df, column_name):
    mean_value = df[column_name].mean()
    std_value = df[column_name].std()
    df[column_name] = (df[column_name] - mean_value) / std_value
    return df

# 对列'Age','Crossing','Finishing'进行z-score 规范化处理
df = z_score_normalization(df, 'Age')
df = z_score_normalization(df, 'Crossing')
df = z_score_normalization(df, 'Finishing')

# 输出结果
print(df[['Age', 'Crossing', 'Finishing']])

# 用箱图显示
sns.boxplot(data=df[['Age', 'Crossing', 'Finishing']])
plt.title('Boxplot of Z-score Normalized Age, Crossing, and Finishing')
plt.show()