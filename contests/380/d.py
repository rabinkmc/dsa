# problem b
from typing import List
import bisect


def sindex(s, a):
    indices = []
    ns = len(s)
    na = len(a)

    for i in range(ns - na + 1):
        if s[i : i + na] == a:
            indices.append(i)
    return indices

def lte(s,i, k):
    i2 = bisect.bisect(s, i+k) 
    i1 = bisect.bisect(s, i - k - 1)
    return i1, i2

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        sa = sindex(s, a)
        sb = sindex(s, b)
        ans = []
        lo = 0
        search = sa
        na = len(sa)
        for i in sb:
            lo, hi = lte(search, i, k)
            ans = ans + search[lo:hi]
            search = search[hi:] 
            if len(ans) == na:
                return ans
        return ans


ans = Solution().beautifulIndices(
    s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15
)

print(ans)
ans = Solution().beautifulIndices(s="abcd", a="a", b="a", k=4)
print(ans)
ans = Solution().beautifulIndices(s = "lnoffflno", a="lno", b="f", k=3)
print(ans)
