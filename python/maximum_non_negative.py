from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # (min, max)
        M = 1000_000_007
        max_dp = [[-float("inf")] * n for _ in range(m)]
        min_dp = [[float("inf")] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                gij = grid[i][j]
                if i == 0 and j == 0:
                    max_dp[i][j] = grid[i][j]
                    min_dp[i][j] = grid[i][j]
                elif i == 0:
                    max_dp[i][j] = max(
                        gij * max_dp[i][j-1],
                        gij * min_dp[i][j-1], 
                    )
                    min_dp[i][j] = min(
                        gij * max_dp[i][j-1],
                        gij * min_dp[i][j-1], 
                    )
                elif j == 0:
                    max_dp[i][j] = max(
                        gij * max_dp[i-1][j],
                        gij * min_dp[i-1][j],
                    )
                    min_dp[i][j] = min(
                        gij * max_dp[i-1][j],
                        gij * min_dp[i-1][j],
                    )
                else:
                    max_dp[i][j] = max(
                        gij * max_dp[i-1][j],
                        gij * min_dp[i-1][j],
                        gij * max_dp[i][j-1],
                        gij * min_dp[i][j-1], 
                    )
                    min_dp[i][j] = min(
                        gij * max_dp[i-1][j],
                        gij * min_dp[i-1][j],
                        gij * max_dp[i][j-1],
                        gij * min_dp[i][j-1], 
                    )
        result = max_dp[m-1][n-1]
        if result < 0:
            return -1
        return result % M # type: ignore


grid = [
    [-1,-2,-3],
    [-2,-3,-3],
    [-3,-3,-2]
]
ans = Solution().maxProductPath(grid)
print(ans)
        
