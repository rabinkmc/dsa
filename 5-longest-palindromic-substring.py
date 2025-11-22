class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # palindrome of even length are also true by
        # deafult

        start = 0
        end = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                end = i + 1

        # now palindrome length > 2
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = s[i] == s[j] and (dp[i + 1][j - 1])
                if dp[i][j]:
                    start = i
                    end = j
        return s[start : end + 1]


print(Solution().longestPalindrome("babad"))
