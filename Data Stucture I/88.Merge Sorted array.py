nums1 = [1, 2, 3, 5, 6, 7]
nums2 = [2, 3, 4]
m = 3
n = 3
if m < 1:  # nums1 沒東西 , 把 nums2[n] 丟給 nums1
    nums1 = nums2[:n]
elif n < 1:  # nums2 沒東西 , nums1 = nums1
    nums1 = nums1[:m]
else:  # 兩個都有東西
    nums1 = sorted(nums1[:m] + nums2[:n])
print(nums1)
'''
s = ''
for i in nums2:
    print(i)
    nums1.append(i)
    # print(nums1)
nums1.sort()

for i in nums1:
    if nums1[i] == 0:
        del nums1[i]
print(nums1)
# for i in range(0,len(nums1) - 1):
#   for j in range(len(nums1))
'''
