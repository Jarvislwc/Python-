nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
new_append = []  # 最後要 return 回去的
# 把一樣的印出來 -> Return [2,2]
# 先判斷哪一個陣列的長度比較短，
'''
new_nums1 = set(nums1)
new_nums2 = set(nums2)   
a = len(nums1) # nums1 長度
b = len(nums2) # nums2 長度
if a > b : # nums1 比較小
    return new_nums1.intersection(new_nums2)
else : 
    return new_nums2.intersection(new_nums1)

new_nums1 = set(nums1)
new_nums2 = set(nums2)
a = len(nums1)  # nums1 長度
b = len(nums2)  # nums2 長度
if a > b:  # nums1 比較小
    c = new_nums1.intersection(new_nums2)
else:
    c = new_nums2.intersection(new_nums1)
print(list(c))
'''
