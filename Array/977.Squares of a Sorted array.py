class Solution:
    def sortedSquares(self, nums):
        '''
        nus = []
        for i in range(len(nums)):
            a = pow(nums[i],2)
            nus.append(a)
            b = sorted(nus)
        return b
        '''
        for i in range(len(nums)):
            nums[i] = (nums[i])**2
        nums.sort()

        return nums
        '''
        for i in range(len(nums)):
            nums[i] = (nums[i])**2
            
        nums.sort()
        
        return nums
            #print(a)
        '''
