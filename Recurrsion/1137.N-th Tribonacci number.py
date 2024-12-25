class Solution:
    def tribonacci(self, n: int) -> int:
        a = 1
        b = 1
        c = 2
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            for i in range(n - 3):
                a, b, c = b, c, a + b + c
            return c
