from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        psum = [0] * (n + 1)
        psum[1] = 1
        for i in range(1, n):
            if s[i] == "1":
                psum[i + 1] = psum[i]
                continue
            l = max(0, i - maxJump)
            r = i - minJump
            if l <= r:
                count = psum[r + 1] - psum[l]
                dp[i] = count > 0
            psum[i + 1] = psum[i] + int(dp[i])
        return dp[n - 1]


s = "011010"
minJump = 2
maxJump = 3
ans = Solution().canReach(s, minJump, maxJump)
print(ans)
