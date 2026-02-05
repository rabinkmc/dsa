from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    continue
                elif r == 0 and c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = (dp[r - 1][c] if r > 0 else 0) + (
                        dp[r][c - 1] if c > 0 else 0
                    )
        return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ans = Solution().uniquePathsWithObstacles(
    obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
)
print(ans)
