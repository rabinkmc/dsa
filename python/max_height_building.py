from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        INF = 2 * 10**9
        r = [INF] * n
        r[0] = 0
        for label, val in restrictions:
            r[label - 1] = val

        for i in range(1, n):
            r[i] = min(r[i], r[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            r[i] = min(r[i], r[i + 1] + 1)
        return max(r)


n = 5
restrictions = [[2, 1], [4, 1]]
n = 6
restrictions = []
ans = Solution().maxBuilding(n, restrictions)
print(ans)
