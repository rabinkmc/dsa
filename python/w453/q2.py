from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        first = complexity[0]
        n = len(complexity)
        out = 1
        for i in range(1, n):
            if complexity[i] <= first:
                return 0

        def dp(n):
            a = 1
            b = 1
            for i in range(2, n + 1):
                a, b = b, i * b
            return b

        ans = dp(n - 1)
        return ans


complexity = [0, 0, 2]
ans = Solution().countPermutations(complexity)
print(ans)
