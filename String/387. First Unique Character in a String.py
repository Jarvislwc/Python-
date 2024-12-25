from numpy import empty


s1 = "leetcode"
s2 = "iloveleetcode"
s3 = 'aabb'
# Given a string s, find the first non-repeating character in it and return its index.
# 找出沒有重複的字串
empty1 = []
dup = []
a = 0
# print(len(s1))
# 找到一個不一樣的 只要找到就 append 進去 然後馬 上break
# return list 長度就好
for i in s2:
    empty1.append(i)
    # empty1 = ['l','e','e','t','c','o','d','e']
    # 沒有重複的 = [l,t,c,o,d]
    # return 第一個
print(empty1)
for j in range(1, len(s2)):
    if empty1[a] == empty1[j]:
        continue
    else:
        dup.append(empty1[a])
    a += 1
'''
dict1 = Counter(s1)

for i in s1: 
    if dict1[i] == 1
        return s1.index(i)
return -1
'''
