class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # Case 1 如果有找到就看他在哪個位子
        # Case 2 如果沒找到用BubbleSort來排位子
        # 回傳位置 就好所以Retrun i

        # print(nums[-1])

        if target <= nums[0]:  # Input最小
            return 0
        elif target > nums[-1]:  # Input最大
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:  # 查找
                return i
