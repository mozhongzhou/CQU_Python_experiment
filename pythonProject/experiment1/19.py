# yyf_experiment1
import pandas as pd
import numpy as np
# 读取CSV文件
df = pd.read_csv('ocean_temp.csv', encoding='utf-8')

# 预览前5行数据
print(df.head())

# 统计数据基本统计量
print(df.describe())

# 创建一个从10到50行的片段
df_slice = df.iloc[10:51]
print(df_slice)