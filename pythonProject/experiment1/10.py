# yyf_experiment1
# 获取用户输入
lstA = list(map(int, input("请输入listA列表，用逗号分隔：").split(',')))
lstB = list(map(int, input("请输入listB列表，用逗号分隔：").split(',')))

# 使用zip函数和dict函数将两个列表组合成一个字典
result = dict(zip(lstA, lstB))

print(result)