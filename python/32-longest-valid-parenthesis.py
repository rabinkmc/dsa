class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        n = len(s)
        dp = [0 for _ in range(len(s))]
        ans = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = 2 + (dp[i-2] if i - 2 >= 0 else 0 )
                else:
                    if s[i - dp[i-1] - 1] == "(":
                        dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1] - 2] if (i - dp[i-1] >= 2 ) else 0)
                ans = max(ans, dp[i])

        return max(dp)
        
ans = Solution().longestValidParentheses(")()())")
print(ans)
