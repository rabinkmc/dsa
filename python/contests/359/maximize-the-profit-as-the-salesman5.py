from typing import List
import bisect
from collections import defaultdict

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        m = [[] for _ in range(n)]
        for s,e,g in offers:
            m[e].append([s,g])
        for e in range(1, n + 1):
            dp[e] = dp[e - 1]
            import ipdb;ipdb.set_trace()
            for s, g in m[e - 1]:
                dp[e] = max(dp[e], dp[s] + g)
        return dp[-1]


n = 5
# offers = [
#     [0, 6, 9],
#     [0, 10, 5],
#     [2, 4, 1],
#     [2, 6, 6],
#     [3, 8, 5],
#     [4, 5, 1],
#     [5, 5, 10],
#     [5, 10, 8],
#     [7, 11, 9],
#     [8, 11, 5],
# ]

offers = [
    [0, 0, 6],
    [0, 1, 5],
    [0, 2, 8],
    [0, 3, 2],
    [0, 3, 7],
    [1, 2, 8],
    [2, 2, 5],
    [2, 3, 2],
    [2, 3, 10],
]

ans = Solution().maximizeTheProfit(n, offers)
print(ans)
