from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [ [0]*(i+1) for i in range(n)]
        dp[0][0] = triangle[0][0]

        def cost(i, j):
            if j == 0:
                return dp[i-1][j]
            if j == i:
                return dp[i-1][j-1]
            return min(dp[i-1][j-1], dp[i-1][j])

        for i in range(1,n):
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + cost(i,j)
        return min(dp[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
ans = Solution().minimumTotal(triangle)
print(ans)
        
