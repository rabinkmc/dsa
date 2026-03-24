class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        end = 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
                start = i
                end = i + 1

        for diff in range(2, n):
            # j is end index
            for i in range(n - diff):
                # i is start index
                # so if you start at i and end at j
                # what do you have to consider for being a palindrome
                # say j is 2
                # that means
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    end = j
        return s[start : end + 1]
