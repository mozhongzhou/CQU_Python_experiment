def yyf_experiment1(A, B):
    return int(str(A) * B)
# 读入两个正整数 A 和 B
A = int(input("请输入一个正整数 A (1 <= A <= 9): "))
B = int(input("请输入一个正整数 B (1 <= B <= 10): "))
# 生成数字
result = yyf_experiment1(A, B)
# 输出结果
print(f"产生的数字为：{result}")
