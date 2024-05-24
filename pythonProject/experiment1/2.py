# 将所有小写字母转换为大写字母
def yyf_experiment1_to_upper_case(s):
    return s.upper()

# 将所有大写字母转换为小写字母
def yyf_experiment1_to_lower_case(s):
    return s.lower()

# 将第一个字母转换为大写字母，其余小写
def yyf_experiment1_capitalize_first_letter(s):
    return s.capitalize()

# 将每个单词的第一个字母转换为大写，其余小写
def yyf_experiment1_capitalize_words(s):
    return s.title()

# 测试字符串
s = "hElLo pYtHOn "

# 输出结果
print("1)", yyf_experiment1_to_upper_case(s))
print("2)", yyf_experiment1_to_lower_case(s))
print("3)", yyf_experiment1_capitalize_first_letter(s))
print("4)", yyf_experiment1_capitalize_words(s))
