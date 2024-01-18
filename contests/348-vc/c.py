from typing import List

"""
1. initialize intialize matrix with 0
2. then, update matrix values
3. at the end sum the values
"""

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # find last queries only
        qs = []
        visited = set()
        for typ, idx, val in queries[::-1]:
            node = (typ, idx)
            if node in visited:
                continue
            if len(visited) == 2*n:
                break
            qs.append((typ,idx, val))
            visited.add(node)

        # apply the queries
        mat = [[0]*n for _ in range(n)]
        for i in range(len(qs) - 1, -1, -1):
            typ, idx, val = qs[i]
            if typ == 0:
                for c in range(n):
                    mat[idx][c] = val
            else:
                for r in range(n):
                    mat[r][idx] = val

        # calculate total 
        total = 0
        for i in range(n):
            for j in range(n):
                total += mat[i][j]
        return total






n = 3
queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
n = 3
queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
print(Solution().matrixSumQueries(n, queries))
        
