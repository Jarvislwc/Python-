'''
n = 12
if n < 10:
    print(False)
else:
    sum1 = n
    while sum1 != 1:
        a = (sum1 // 10)**2
        b = (sum1 % 10)**2
        sum1 = sum1 + (a + b)
        print("a + b = ", a, b, sum1)
        '''
seen = set()  # 用來記錄已經出現過的數字，以檢查是否進入循環
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(digit) ** 2 for digit in str(n))

print(n == 1)
