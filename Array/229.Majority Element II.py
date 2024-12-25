from collections import Counter
nums1 = [3, 2, 3]
res = []
# print(len(nums1))
len_of_nums = len(nums1)//3
s = Counter(nums1)
# Counter = {3 : 2,2 : 1}
# s[i] 後面兩個數
# i 就是前面兩個
for i in s:
    if s[i] >= len_of_nums:
        res.append(i)
        # print(s[i])
# print(res)
print(len(nums1)/3)  # 這個會有 float 的問題
print(len(nums1)//3)  # 這個是直接取 int 的部分
'''
res = []
len_of_nums = len(nums)//3
s = Counter(nums)
for i in s:    
    if s[i] > len_of_nums:
        res.append(i)
return res
'''
