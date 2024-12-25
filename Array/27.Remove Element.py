nums = [0, 1, 2, 2, 3, 0, 4, 2]
'''
# 1. 找出重複的數值
# 2. 刪除重複數值
# 3. 刪完數值後，其他數值要往前移，然後後面要空出來
# 4. 也就是說，刪完的空間依然要留著，不會不見
# 5. 返回刪除後，陣列裡面的數值
count = 0
equal = nums[0]
for i in range(0, len(nums)-1):
    for j in range(i + 1, len(nums)):
        if(nums[i] == nums[j]):
            equal = nums[i]  # 找出出現最多次的數值
            count += 1
#        if nums[i] == equal:  # 這邊要把出現最多次的數值給刪除
#            del nums[i]
print(nums)

if not nums:
    print("0")
i, j = 0, 1
# nums 的長度為 n
# j 就是從1 ~ n-1
# i 不管
while j < len(nums):  # 當J小於nums的長度
    if nums[i] != nums[j]:  # 如果nums[i]的數值 跟 nums[j] 不一樣
        i += 1  # i 往前一格
        nums[i] = nums[j]  # 把 nums[j] 的值 給 nums[i]
    j += 1  # j 往前一格直到 j == len(nums)
print(i + 1)  # 最後返回 i 的數值
'''


def removeElement(self, nums, val: int) -> int:
    # 1. 找出重複的數值
    # 2. 刪除重複數值
    # 3. 刪完數值後,其他數值要往前移,然後後面要空出來
    # 4. 也就是說,刪完的空間依然要留著,不會不見

    while val in nums:
        nums.remove(val)
    return len(nums)
