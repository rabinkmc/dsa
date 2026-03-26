class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        m = len(s)
        n = len(p)

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == n:
                ans = i == m
                memo[i, j] = ans
                return ans
            first_match = i < len(s) and p[j] in {s[i], "."}
            if j + 1 < len(p) and p[j + 1] == "*":
                ans = dp(i, j + 2) or first_match and dp(i + 1, j)
            else:
                ans = first_match and dp(i + 1, j + 1)
            memo[i, j] = ans
            return ans

        return dp(0, 0)


s = "aa"
p = "a*"
ans = Solution().isMatch(s, p)
print(ans)
