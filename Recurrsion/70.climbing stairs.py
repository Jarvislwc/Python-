# 70.climbing stairs
# 你正在爬樓梯，需要走n部才能爬到頂
# 你每次可以爬一步或兩部，你有多少方法可以爬到頂呢？
# 算出每次相加到 Target 的總和
# 2 = 1 + 1 / 2 (2 種)
# 3 = 1 + 1 + 1 / 1 + 2 / 2 + 1 (for
# 4 = 1 + 1 + 2 / 1 + 2 + 1 / 1 + 1 + 1 + 1 / 2 + 1 + 1 / 2 + 2  (5種)
# 5 = 1 + 2 + 1 + 1 / 1 + 1 + 2 + 1 / 1 + 1 + 1 + 2 / 1 + 2 + 2 / 2 + 1 + 2 / 2 + 1 + 1 + 1 / 2 + 2 + 1 (8種)
# 費氏數列
def fiz(a):
    if a == 1:
        return 1
    elif a == 0:
        return 0
    else:
        return fiz(a - 2) + fiz(a - 1)
    return a

a = int(input("plz input your number:"))
print(fiz(a))
#================================================
class Solution:
    def climbStairs(self, n: int) -> int:
        # 你正在爬樓梯，需要走n部才能爬到頂 
        # 你每次可以爬一步或兩部，你有多少方法可以爬到頂呢？
        # 算出每次相加到 Target 的總和
        # 2 = 1 + 1 / 2 
        # 3 = 1 + 1 + 1 / 1 + 2 / 2 + 1  
        # 4 = 1 + 2 + 1 / 1 + 1 + 2 / 1 + 1 + 1 + 1 / 2 + 1 + 1 / 2 + 2  
        #Solution 
        # 費氏數列變形版
        # 前兩個數字加起來
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2 :
            return 2
        a = 2
        b = 3 
        
        for i in range(n - 3): 
            b , a = a + b, b
        return b         
            # return self.climbStairs(n - 2) + self.climbStairs(n - 1)
        
