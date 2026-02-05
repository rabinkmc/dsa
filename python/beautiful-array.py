from functools import lru_cache
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        @lru_cache(None)
        def dfs(n):
            if n == 1:
                return [1]
            left = dfs((n + 1) // 2)
            right = dfs(n // 2)
            print(f"  {left=}, {right=}")

            odd = [x * 2 - 1 for x in left]
            even = [x * 2 for x in right]
            return odd + even

        return dfs(5)


n = 5
print(Solution().beautifulArray(n))
