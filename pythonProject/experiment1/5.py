# yyf_experiment1
height = 1.75
weight = 80.5
# 计算BMI指数
bmi = weight / (height ** 2)

# 判断并打印结果
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")