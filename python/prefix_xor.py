from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        out = [pref[0]]
        n = len(pref)
        for i in range(1, n):
            out.append(pref[i] ^ pref[i - 1])
        return out


pref = [5, 2, 0, 3, 1]
ans = Solution().findArray(pref)
print(ans)
