# 26.Remove Duplicates from Sorted Array
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# ================================Question===============================================
# Given an integer array nums sorted in non-decreasing order, 給一個遞增排序的陣列
# remove the duplicates in-place such that each unique element appears only once. 利用in-place 方法移除掉陣列裡元素好讓朕咧裡每個元素都是唯一
# The relative order of the elements should be kept the same. 最後回傳的元素也須按照原陣列排序
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
dup = 1
# 解題想法
# 從第二個數字開始找 (for)
# 如果 “第二個數字” (nums[i]) 跟 “第一個數字” nums(i+1) 不一樣的話，
# 長度就 + 1 (dup = dup + 1)
# 並且把第二個數字改成被比較的數字。(nums[dup] = nums[i])
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[dup] = nums[i]
        dup += 1
print(" 返回的長度: ", dup)
