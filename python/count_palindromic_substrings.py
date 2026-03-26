class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = n
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j]:
                    ans += 1
        return ans


s = "babad"
ans = Solution().countSubstrings(s)
print(ans)
