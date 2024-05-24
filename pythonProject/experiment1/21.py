# yyf_experiment1
import pandas as pd
import numpy as np
# 读取CSV文件
df = pd.read_csv('ocean_temp.csv', encoding='utf-8')

# 从数据框df创建一个数组
tempArr = np.array(df)

# 创建一个与tempArr大小相同，所有元素都设置为20的数组
adjar = np.full_like(tempArr, 20)

# 将两个数组添加到一个新的数组中
newTemp = np.vstack((tempArr, adjar))

# 定义一个函数，将温度从华氏度转换为摄氏度
def f_to_c(F):
    return (5/9) * (F - 32)

# 使用矢量化函数将newTemp中的所有温度数据转换为摄氏度
cTemp = f_to_c(newTemp)

# 显示上述所有数组的前50个元素
print('newTemp:\n', newTemp[:50])
print('cTemp:\n', cTemp[:50])

# 显示上述cTemp数据的20到50行
print('cTemp (20 to 50):\n', cTemp)