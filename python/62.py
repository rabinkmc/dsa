"""

X 0 1 2 3 4 5 6 7 
0 0 0 0 0 0 0 0 0 
1 0 1 1 1 1 1 1 1
2 0 1 2 3 4 5 6 7
3 0 1 3 6 10 15 21 28


"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (i, j) == (1, 1):
                    continue
                dp[i][j] =  dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

m = 3 
n = 7 
print(Solution().uniquePaths(m,n))


