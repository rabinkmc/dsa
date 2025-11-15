class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n <= 2:
                return n
            ans = helper(n-1) + helper(n-2)
            memo[n] = ans
            return ans
        return helper(n)

print(Solution().climbStairs(5))
        
