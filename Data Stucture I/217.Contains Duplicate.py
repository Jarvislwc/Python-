class Solution:
    def containsDuplicate(self, nums):
        # 如果一個陣列中，有Value 出現兩次 就Return true 反之 False 
        # count = [] # 計算數字的
        #return len(set(nums)) != len(nums)
        if len(nums) != len(set(nums)):
            return True 
        else :
            return False
        