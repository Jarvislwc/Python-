
from unicodedata import digit


num = [1, 3, 2, 1]
k = 34
newnumber = []  # 最後放新數字
temp = ''.join(str(s) for s in num)
tSum = int(temp) + k
# 把Sum裡面的東西再轉成數字
for i in str(tSum):  # 只能是字串 回圈裡不能放不能迭代的東西 數字不行 因為他不能迭代 所以要再轉成數字
    newnumber.append(int(i))  # 再轉成 數字丟進去
print(newnumber)
'''
for i in num:
    newword = str(i)
    print(newword)
    a = int(newword)
    strs = str(a + k)
print(strs)
# for i in strs:
#    newnumber.append(int(i))
# print(newnumber)
'''
