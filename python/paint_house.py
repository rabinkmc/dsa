from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[float("inf")] * 3 for _ in range(n)]
        for j in range(3):
            dp[0][j] = costs[0][j]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        return min(dp[-1])

    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [[float("inf")] * 3 for _ in range(n)]
        print(k)
        for j in range(k):
            dp[0][j] = costs[0][j]
        for i in range(1, n):
            for j in range(k):
                for l in range(k):
                    if l == j:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i - 1][l])
                dp[i][j] += costs[i][j]
        return min(dp[-1])


costs = [[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]
costs = [[1, 3], [2, 4]]
costs = [[17, 9, 6, 2, 6, 18, 8, 12, 3, 5, 9, 11, 20, 8, 13, 16]]
ans = Solution().minCostII(costs)
print(ans)
