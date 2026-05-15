from typing import List


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        INF = 2 * 1000_000_000
        r = [INF] * n
        r[0] = 0
        for idx, val in restrictions:
            r[idx] = val
        for i in range(1, n):
            r[i] = min(r[i], r[i - 1] + diff[i - 1])

        for i in range(n - 2, -1, -1):
            r[i] = min(r[i], r[i + 1] + diff[i])
        return max(r)


n = 10
restrictions = [[3, 1], [8, 1]]
diff = [2, 2, 3, 1, 4, 5, 1, 1, 2]
ans = Solution().findMaxVal(n, restrictions, diff)
print(ans)
