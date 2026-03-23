from functools import lru_cache

@lru_cache(None)
def f(x):
    if x == 1:
        return 0
    mid = x // 2
    if x % 2 == 0:
        return f(mid) + f(mid) + mid * mid
    else:
        return f(mid) + f(mid + 1) + mid * (mid + 1)

class Solution:
    def minCost(self, n: int) -> int:
        return f(n)

n = 4
ans = Solution().minCost(n)
print(ans)
        
