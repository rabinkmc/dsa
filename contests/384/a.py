from typing import List
from functools import cache

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        @cache
        def get_max(col):
            ans = -2
            for i in range(m):
                ans = max(ans, matrix[i][col])
            return ans

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1: 
                    matrix[i][j] = get_max(j)
        return matrix





        
