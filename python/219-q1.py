class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans = ans + n // 2
            if n % 2 == 1:
                n = (n + 1) // 2
            else:
                n = n // 2
        return ans


n = 3
ans = Solution().numberOfMatches(n)
print(ans)
