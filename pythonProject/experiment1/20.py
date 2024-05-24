# yyf_experiment1
import pandas as pd
import numpy as np
# 读取CSV文件
df = pd.read_csv('ocean_temp.csv', encoding='utf-8')

# 从数据框df创建一个数组
tempArr = np.array(df)

# 输出数组的大小和类型
print('Size of tempArr:', tempArr.size)
print('Type of tempArr:', tempArr.dtype)