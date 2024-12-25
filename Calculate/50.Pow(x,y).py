class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return pow(x,n)
        # 平方怎麼求
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return self.myPow(x, n - 1) * 2
