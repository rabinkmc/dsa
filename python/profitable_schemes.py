from typing import List
from functools import lru_cache


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        group_size = len(group)

        @lru_cache(None)
        def dp(i, size, p):
            if i == group_size:
                if p >= minProfit:
                    return 1
                else:
                    return 0
            skip = dp(i + 1, size, p)
            take = 0
            if size >= group[i]:
                take = dp(i + 1, size - group[i], min(minProfit, p + profit[i]))
            return (take + skip) % 1000_000_007

        return dp(0, n, 0)


n = 5
minProfit = 3
group = [2, 2]
profit = [2, 3]

# n = 1
# minProfit = 1
# group = [2, 2, 2, 2, 2]
# profit = [1, 2, 1, 1, 0]
ans = Solution().profitableSchemes(n, minProfit, group, profit)
print(ans)
