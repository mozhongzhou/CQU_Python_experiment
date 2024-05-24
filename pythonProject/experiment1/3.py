def yyf_experiment1_find_letters(input_string):
    letters = []
    for char in input_string:
        if char.isalpha():
            if char.lower() not in letters:
                letters.append(char.lower())
            if len(letters) == 10:
                return letters
    return "not found"

s =input("请输入一个字符串: ")
print(yyf_experiment1_find_letters(s))