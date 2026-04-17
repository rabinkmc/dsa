from typing import List
from heapq import heappush, heappop


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        pq = []
        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Formula: Current + Top + Left ^ Top-Left (to cancel double-count)
                # matrix[i-1][j-1] because the matrix is 0-indexed
                pref[i][j] = (
                    matrix[i - 1][j - 1]
                    ^ pref[i - 1][j]
                    ^ pref[i][j - 1]
                    ^ pref[i - 1][j - 1]
                )
                heappush(pq, pref[i][j])
                if len(pq) > k:
                    heappop(pq)
        return pq[0]


matrix = [[5, 2], [1, 6]]
k = 1
matrix = [[5, 2], [1, 6]]
k = 3
ans = Solution().kthLargestValue(matrix, k)
print(ans)
