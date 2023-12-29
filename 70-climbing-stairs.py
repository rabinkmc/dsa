class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a+b
        return b
        

assert Solution().climbStairs(n=2) == 2
assert Solution().climbStairs(n=3) == 3, Solution().climbStairs(n=3)
assert Solution().climbStairs(n=5) == 8, Solution().climbStairs(n=5)
