class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(1, 6):
            ans += n // ( 5**i)
        return ans

ans = Solution().trailingZeroes(100)
print(ans)

        
