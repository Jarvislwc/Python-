from collections import Counter
s = "a"
t = "ab"
dict1 = Counter(s)
# 如果 s 的字元沒有在 t 裡面 就Return false
# 兩個字元相相比較，如果比對結果失敗，Return False
for char in t:
    print("char:", char)
    if char not in dict1:
        print(False)

    else:
        dict1[char] -= 1
        print("charnumber:", dict1[char])
        if dict1[char] < 0:
            print(False)
print(True)
