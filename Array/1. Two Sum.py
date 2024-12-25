
class Solution:
    def twoSum(self, nums, target: int):
        '''
        num 0 + num 1 = target
        num 0 + num 2  
        ......
        num 1 + num 2
        num 2 + num 3
        現在是卡在 我過了第一關後 code會直接卡住 第二道測驗過不了 
        所以我要開一個迴圈 避免這個情況發生(然後不能寫兩個For迴圈)
        這樣是O(n2)
        '''
        j = 1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
