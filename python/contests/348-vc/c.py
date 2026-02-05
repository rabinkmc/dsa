from typing import List

"""
1. initialize intialize matrix with 0
2. then, update matrix values
3. at the end sum the values
"""

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        cols, rows = set(), set()
        total = 0
        for typ, idx, val in queries[::-1]:
            if typ:
                if idx not in cols:
                    cols.add(idx)
                    # since I am doing it in reverse
                    # I shouldn't take the cells which have already been updated
                    # suppose I am visiting 1st column and 2 rows have already been affected
                    # then, only value that I can replace is the one that has not been affected 
                    # or only cell that contributes to total is the one that hasn't been updated yet
                    total += val * (n - len(rows))
            else:
                if idx not in rows:
                    rows.add(idx)
                    total += val * (n - len(cols))
        return total






n = 3
queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
n = 3
queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
print(Solution().matrixSumQueries(n, queries))
        
