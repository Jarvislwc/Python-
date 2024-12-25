from re import L


nums = [1, 5, 7, 0, 43, 1, 0, 18]

non_zero_index = 0

# 記錄有幾個非0數字
for i in range(len(nums)):
    if nums[i] != 0:
        nums[non_zero_index] = nums[i]
        non_zero_index += 1

# 後面補0 幹 超聰明...
while non_zero_index < len(nums):
    nums[non_zero_index] = 0
    non_zero_index += 1

print(non_zero_index)
print(nums)
