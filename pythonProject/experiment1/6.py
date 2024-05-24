# yyf_experiment1
# 获取用户输入
num = input("请输入一个数字：")

# 计算各个位数之和
sum_of_digits = sum(int(digit) for digit in num)

# 判断各个位数之和是奇数还是偶数
if sum_of_digits % 2 == 0:
    print(num)
else:
    print(num[::-1])  # 倒序打印数字