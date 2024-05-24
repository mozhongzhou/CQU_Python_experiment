# yyf_experiment1
# 获取用户输入
num = int(input("请输入一个数字："))

# 计算阶乘
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"{num}的阶乘是：{factorial}")