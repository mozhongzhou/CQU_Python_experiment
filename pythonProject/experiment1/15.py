# yyf_experiment1
# 初始化鱼的数量
fish = 5

while True:
    total = fish
    # 对每个人进行操作
    for _ in range(5):
        # 不能做到分五份恰好余1就不行
        if total % 5 != 1 :
            break
        # 否则，扔掉一条鱼，然后分给一个人
        total = (total-1) // 5 * 4
    else:
        # 如果所有的人都满足条件，那么就找到了答案
        print(f"他们至少捕了{fish}条鱼")
        break

    # 如果没有找到答案，那么就增加鱼的数量
    fish += 1