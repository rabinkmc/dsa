from typing import List
from bisect import bisect_left


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        def diff(bar, size):
            ans = set()
            bar.sort()
            bars = [1, *bar, size]
            for i in range(len(bars)):
                for j in range(i + 1, len(bars)):
                    ans.add(bars[j] - bars[i])

            return ans

        hbar_diffs = diff(hFences, m)
        vbar_diffs = diff(vFences, n)
        diffs = hbar_diffs & vbar_diffs
        if not diffs:
            return -1
        ans = max(diffs)
        modulo = 1000000007
        return (ans**2) % modulo


m = 6
n = 7
hBars = [2]
vBars = [4]

print(Solution().maximizeSquareArea(m, n, hBars, vBars))
