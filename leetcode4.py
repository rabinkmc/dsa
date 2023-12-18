from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        def get_range(bars):
            bars.sort()
            ans = 1
            i = 1
            temp = 2 if bars else 1
            for i in range(1, len(bars)):
                if bars[i] - bars[i - 1] == 1:
                    temp += 1
                else:
                    temp = 2
                ans = max(ans, temp)

            return max(ans, temp)

        hrange = get_range(hBars)
        vrange = get_range(vBars)
        return min(hrange, vrange) ** 2


n = 2
m = 4
hBars = [3, 2]
vBars = [4, 2]

n1 = 2
m1 = 1
hBars1 = [2, 3]
vBars2 = [2]

print(Solution().maximizeSquareHoleArea(n, m, hBars, vBars))
print(Solution().maximizeSquareHoleArea(n1, m1, hBars1, vBars2))
