# yyf_experiment1
A = [("dog", "type"), ("black", "color"), ("cat", "type"), ("blue", "color"), ("green", "color"), ("pig", "type")]

# 提取所有的颜色值
A_colors = [item[0] for item in A if item[1] == "color"]

# 输出列表 A_colors
print("A_colors:", A_colors)