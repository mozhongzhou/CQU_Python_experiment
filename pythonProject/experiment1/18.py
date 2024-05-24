# yyf_experiment1
import pandas as pd

# 创建一些序列
s1 = pd.Series([1, 4], name='a')
s2 = pd.Series([2, 5], name='b')
s3 = pd.Series([3, 6], name='c')

# 使用这些序列创建一个二维表
d = pd.concat([s1, s2, s3], axis=1)

print(d)