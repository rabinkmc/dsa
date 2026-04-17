from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]
        ans = 0
        for i in range(m):
            mat = sorted(matrix[i], reverse=True)
            for j in range(n):
                ans = max(ans, (j + 1) * mat[j])
        return ans


matrix = [[1, 1, 0], [1, 0, 1]]
ans = Solution().largestSubmatrix(matrix)
print(ans)
