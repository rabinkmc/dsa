from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        psum = [0]
        curr = 0
        for candy in candiesCount:
            curr += candy
            psum.append(curr)
        out = []
        for candy_i, day_i, cap in queries:
            if day_i + 1 > psum[candy_i + 1]:
                out.append(False)
            elif psum[candy_i] + 1 > cap * (day_i + 1):
                out.append(False)
            else:
                out.append(True)
        return out


candiesCount = [7, 4, 5, 3, 8]
queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
ans = Solution().canEat(candiesCount, queries)
print(ans)
