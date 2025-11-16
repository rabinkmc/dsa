from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i):
            if i >= n - 1:
                return 1
            if s[i] == "0":
                return 0
            ans = dp(i + 1)
            if 11 <= int(s[i : i + 2]) <= 26:
                ans += dp(i + 2)
            return ans

        return dp(0)


print(Solution().numDecodings("226"))
