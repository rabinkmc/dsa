from functools import lru_cache
import math


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if startPos > endPos:
            startPos, endPos = endPos, startPos
        R = endPos - startPos
        if R > k:
            return 0
        if R % 2 != k % 2:
            return 0
        M = 1000_000_007

        L = (k - R) // 2
        R = R + L
        return math.comb(k, R) % M


startPos = 1
endPos = 2
k = 3
startPos = 264
endPos = 198
k = 68
ans = Solution().numberOfWays(startPos, endPos, k)
print(ans)
