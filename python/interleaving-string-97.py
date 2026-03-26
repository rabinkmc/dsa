from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        N = m + n

        if len(s3) > N:
            return False

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return s2[j:] == s3[i + j :]
            if j == n:
                return s1[i:] == s3[i + j :]
            state1 = False
            state2 = False
            if s1[i] == s3[i + j]:
                state1 = dp(i + 1, j)
            if s2[j] == s3[i + j]:
                state2 = dp(i, j + 1)
            return state1 or state2

        return dp(0, 0)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
print(Solution().isInterleave(s1, s2, s3))
