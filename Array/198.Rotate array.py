class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = 多少就向右轉多少
        # 只要把最後一個數字移到最前面
        # k = k % len(nums) ->
        # for s in range(0,k):
        n = len(nums)
        if len(nums) < k:  # 如果陣列長度 < k
            k = k % len(nums)  # k/(陣列長度)取餘數
        z = nums[n-k:] + nums[:n-k]
        # nums[n-k:] -> 取後面的值
        # Example 1 : k = 3 ,n = 7
        # -> nums[4:end] = nums[4:6]
        # -> nums[start:4] = nums[0:3]
        # print(len(z))
        for i in range(len(z)):
            nums[i] = z[i]
