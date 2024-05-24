# yyf_experiment2

from scipy.optimize import fsolve

# 定义要求解的方程组
def equations(vars):
    x1, x2 = vars
    eq1 = 5*x1 - x2**2 - 1
    eq2 = x1**2 - x2 - 6
    return [eq1, eq2]

# 输入初值[1, 1]并求解
x1, x2 =  fsolve(equations, (1, 1))

# 输出结果
print(f"x1 = {x1}, x2 = {x2}")