class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h = len(word1) + 1
        w = len(word2) + 1
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = 0

        for r in range(1, h):
            for c in range(1, w):
                cost  = int(word1[r-1] != word2[c-1])
                dp[r][c] = min(dp[r-1][c] + 1, dp[r][c-1] + 1, dp[r-1][c-1] + cost)
        return dp[h-1][w-1]

word1 = "horse"
word2 = "ros"
ans = Solution().minDistance(word1, word2)
print(ans)
