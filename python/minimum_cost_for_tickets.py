from typing import List
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]

        @lru_cache(None)
        def dp(i):
            if i > n:
                return 0

            if i not in days:
                return dp(i + 1)

            day1 = costs[0] + dp(i + 1)
            day7 = costs[1] + dp(i + 7)
            day30 = costs[2] + dp(i + 30)
            return min(day1, day7, day30)

        return dp(1)


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
ans = Solution().mincostTickets(days, costs)
print(ans)
