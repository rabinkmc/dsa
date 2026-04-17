from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = dict()
        for u, v in dominoes:
            if u > v:
                u, v = v, u
            counter[(u, v)] = counter.get((u, v), 0) + 1
        ans = 0
        for val in counter.values():
            if val == 1:
                continue
            ans = ans + val * (val - 1) // 2
        return ans


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
ans = Solution().numEquivDominoPairs(dominoes)
print(ans)
