# yyf_experiment1
# 获取用户输入
nums = list(map(int, input("请输入一个包含若干整数的列表，用逗号分隔：").split(',')))

# 生成新的只包含偶数的列表
even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)