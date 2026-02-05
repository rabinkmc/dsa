from typing import List
from heapq import heappush, heappop

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        rows = [] * m
        for i in range(m):
            rows.append([-mat[i].count(1), -i])
        pq = []
        for i in range(m):
            heappush(pq, rows[i])
            if len(pq) > k:
                heappop(pq)
        res = []
        while pq:
            _, idx = heappop(pq)
            res.append(-idx)
        return res[::-1]

mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
] 
ans = Solution().kWeakestRows(mat, 3)
print(ans)
