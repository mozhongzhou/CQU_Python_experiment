# yyf_experiment1
# 初始化列表
nums = [88, 5, 23, 31, 45, 4, 6, 1, 16, 12]

# 冒泡排序
for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)