prices = [7, 1, 5, 3, 6, 4]
profits = 0
maxprofit = 0  # retrun value
maxprice = prices[-1]
minprice = prices[0]
for i in range(len(prices)):
    if prices[i] < minprice:
        minprice = prices[i]
        # print(minprice)
    for j in range(prices[i], len(prices)):
        if prices[j] > maxprice:
            maxprice = prices[j]
            # print(maxprice)
        profits = maxprice - minprice
        # maxprofit 是上一輪的最大收益
        # profit 是這輪收益
        print("maxprofits:", maxprofit)
        print("profits:", profits)
        if profits > maxprofit:
            maxprofit = profits
        else:
            print(maxprofit)
print("finalmaxprofits:", maxprofit)
# return maxprofit
