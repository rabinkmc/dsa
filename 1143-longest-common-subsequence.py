class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = {} 
        def dp(i, j):
            if i == m:
                return 0
            if j == n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = -1
            if text1[i] == text2[j]:
                ans = 1 + dp(i+1, j+1) 
            else:
                ans = max(dp(i+1, j), dp(i, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)

text1 = "abcdef"
text2 = "acef"
print(Solution().longestCommonSubsequence(text1, text2))
