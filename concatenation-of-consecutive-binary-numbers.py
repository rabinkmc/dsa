def digitShift(i):
    shift = 0
    while i > 0:
        i = i // 2
        shift += 1
    return shift


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 1_000_000_007
        for i in range(1, n + 1):
            ans = ((ans << digitShift(i)) + i) % MOD
        return ans


n = 3
ans = Solution().concatenatedBinary(n)
print(ans)
