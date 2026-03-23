from typing import List
from functools import lru_cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ns = len(strs)

        @lru_cache(None)
        def dp(i, zeros, ones):
            if i == ns:
                return 0

            zc = strs[i].count("0")
            oc = strs[i].count("1")

            if zeros + zc <= m and ones + oc <= n:
                take = 1 + dp(i + 1, zeros + zc, ones + oc)
                skip = dp(i + 1, zeros, ones)
                return max(take, skip)
            else:
                return dp(i + 1, zeros, ones)

        return dp(0, 0, 0)


strs = ["10", "0001", "111001", "1", "0"]
m, n = 5, 3
ans = Solution().findMaxForm(strs, m, n)
print(ans)
