class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h = len(word1) + 1
        w = len(word2) + 1
        dp = [[0 for _ in range(w)] for _ in range(h)]
        dp[0][0] = 0
        for c in range(1, w):
            dp[0][c] = c
        for r in range(1, h):
            dp[r][0] = r

        for r in range(1, h):
            for c in range(1, w):
                cost = int(word1[r - 1] != word2[c - 1])
                dp[r][c] = min(
                    dp[r - 1][c] + 1, dp[r][c - 1] + 1, dp[r - 1][c - 1] + cost
                )
        return dp[h - 1][w - 1]


word1 = "dhmaa"
word2 = "dhamala"
ans = Solution().minDistance(word1, word2)
print(ans)
