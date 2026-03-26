from functools import lru_cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        def ascii_sum(s):
            return sum(ord(ch) for ch in s)

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return ascii_sum(s2[j:])
            if j == n:
                return ascii_sum(s1[i:])
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            return min(ord(s1[i]) + dp(i + 1, j), ord(s2[j]) + dp(i, j + 1))

        return dp(0, 0)


s1 = "delete"
s2 = "leet"

s1 = "sea"
s2 = "eat"
ans = Solution().minimumDeleteSum(s1, s2)
print(ans)
