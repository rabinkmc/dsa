# problem b
from typing import List


def sindex(s, a):
    indices = []
    ns = len(s)
    na = len(a)

    for i in range(ns - na + 1):
        if s[i : i + na] == a:
            indices.append(i)
    return indices


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        sa = sindex(s, a)
        sb = sindex(s, b)
        ans = []
        for i in sa:
            for j in sb:
                if abs(j - i) <= k:
                    ans.append(i)
                    break
        return ans


ans = Solution().beautifulIndices(
    s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15
)

print(ans)
ans = Solution().beautifulIndices(s="abcd", a="a", b="a", k=4)
print(ans)
