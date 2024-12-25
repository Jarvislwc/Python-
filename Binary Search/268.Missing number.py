from re import L


nums1 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums2 = [3, 0, 1]
nums3 = [0, 1]
# Return 8
#nums = nums.sort()
Newnums = sorted(nums3)
print(Newnums)
for i in range(0, len(Newnums)):
    if i != Newnums[i]:
        print("Result:", i)
    else:
        print("Result", i + 1)
