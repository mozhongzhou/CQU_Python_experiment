# yyf_experiment1
# 获取用户输入
num = int(input("请输入一个数字："))

# 转换为字符串以获取位数
str_num = str(num)
n = len(str_num)

# 计算各位数字的n次方之和
sum = 0
for digit in str_num:
    sum += int(digit) ** n

# 检查是否为阿姆斯特朗数
if sum == num:
    print(f"{num}是阿姆斯特朗数")
else:
    print(f"{num}不是阿姆斯特朗数")