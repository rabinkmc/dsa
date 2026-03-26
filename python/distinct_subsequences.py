from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        @lru_cache(None)
        def dp(i, j):
            if i == m or j == n:
                if j == n:
                    return 1
                else:
                    return 0
            if s[i] == t[j]:
                return dp(i + 1, j) + dp(i + 1, j + 1)
            else:
                return dp(i + 1, j)

        return dp(0, 0)


s = "rabbbit"
t = "rabbit"

# s = "babgbag"
# t = "bag"
ans = Solution().numDistinct(s, t)
print(ans)
