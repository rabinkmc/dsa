class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32, 0, -1):
            bit = (n >> (32-i)) & 1
            if bit:
                ans += 2**(i-1)
        return ans


num = 4
ans = Solution().reverseBits(4)
print(ans)
