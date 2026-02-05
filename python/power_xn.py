class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1/p(x, -n)
            if n % 2 == 0:
                return p(x * x, n//2)
            return x*p(x*x, n // 2)
        return p(x, n)
        
ans = Solution().myPow(2, -5)
print(ans)
