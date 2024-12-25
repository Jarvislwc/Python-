prices = [7, 1, 5, 3, 6, 4]
prices1 = [1, 2, 3, 4, 5]
prices2 = [7, 6, 4, 3, 1]
maxofprofit = 0
maxnumber = prices[-1]
minnumber = prices[0]
for i in range(0, len(prices)):
    if prices[i] > maxnumber:  # Testcase 3
        maxnumber = prices[i]
    elif prices[i] < minnumber:
        minnumber = prices[i]
    else:
        maxnumber = 0
# print(maxnumber)
    for j in range(1, len(prices)):
        maxofprofit = prices[j-i]
        if prices[j-1] < prices[j]
