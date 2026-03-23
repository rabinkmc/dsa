from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return 0
            if j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)


text1 = "abcde"
text2 = "ace"
ans = Solution().longestCommonSubsequence(text1, text2)
print(ans)
