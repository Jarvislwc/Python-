import string
digits = [1,3,7,9]
k = 48
res = []  # 最後放新數字
s = ''  # 開空字串

for i in digits:
    s += str(i)
    print(type(s))
    a = int(s)
    print(a)
    strs = str(a + 1)
for i in strs:
    # print(strs[i])
    # print(type(strs))
    res.append(int(i))
print(res)
# print(sum1)
# print(a[0])
