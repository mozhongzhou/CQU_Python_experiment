# yyf_experiment1
# 获取用户输入
setA = set(input("请输入集合A的元素，用逗号分隔：").split(','))
setB = set(input("请输入集合B的元素，用逗号分隔：").split(','))

# 计算并打印交集
print("交集：", setA & setB)

# 计算并打印并集
print("并集：", setA | setB)

# 计算并打印差集
print("差集：", setA - setB)