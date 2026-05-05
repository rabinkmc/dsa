from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        print(list(zip(*mat)))
        return False


mat = [[0, 1], [1, 0]]
target = [[1, 0], [0, 1]]
ans = Solution().findRotation(mat, target)
print(ans)
