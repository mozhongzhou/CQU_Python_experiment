def yyf_experiment1_is_palindrome(s):
    if s == s[::-1]:
        return f"{s}是回文字符串"
    else:
        return f"{s}不是回文字符串"
s = input("回文字符串判断,请输入一个字符串:  ")
print(yyf_experiment1_is_palindrome(s))