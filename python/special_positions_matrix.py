from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rsum = [0] * m
        csum = [0] * n
        for i in range(m):
            rsum[i] = sum(mat[i])
        for j in range(n):
            current = 0
            for i in range(m):
                current += mat[i][j]
            csum[j] = current
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 1:
                    continue
                if rsum[i] == 1 and csum[j] == 1:
                    ans += 1
        return ans


mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
ans = Solution().numSpecial(mat)
print(ans)
