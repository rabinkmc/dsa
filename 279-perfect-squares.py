class Solution:
    def numSquares(self, n: int) -> int:
        squares = [1]
        for i in range(2, n//2 + 1):
            if i * i <= n:
                squares.append(i*i)
        INT_MAX = 10001
        dp = [INT_MAX]*(n+1)
        dp[0] = 0
        for num in squares:
            dp[num] = 1
        for i in range(n+1):
            for num in squares:
                if i - num > 0:
                    dp[i] = min(dp[i], dp[i-num] + dp[num])
        return dp[-1]
        
ans  = Solution().numSquares(4)
print(ans)
