# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
# i 不能等於 j 也不能等 k
# j 不能等於 k
# num[ i + j + k ] = 0
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
nums = [-1, 0, 1, 2, -1, -4]
# range =  0  1  2  3   4   5
# nums = [-1, 0, 1, 2, -1, -4]
new = []
app = []
count = 0
'''
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(i + 2, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                app.append(nums[i])
                count = count + 1
                app.append(nums[j])
                count = count + 1
                app.append(nums[k])
                count = count + 1
                if count == 3:
                    new.append(app)
                    print(new)
                    count = 0
                app.clear()
                # print(new)
            elif i == j | i == k | j == k:
                print("0")
print(new)
'''
nums.sort()
res = []
