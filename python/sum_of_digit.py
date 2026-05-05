class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n:
            rem = n % k
            ans = ans + rem
            n = n // k
        return ans


n, k = 34, 6
ans = Solution().sumBase(n, k)
print(ans)
