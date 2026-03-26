from typing import List
from heapq import heappush, heappop

# dijkstra


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        INF = float("inf")
        dists = [[INF] * n for _ in range(m)]
        dists[0][0] = 0
        q = []
        q.append((0, (0, 0)))
        while q:
            dist, node = heappop(q)
            r, c = node
            if r == m - 1 and c == n - 1:
                return dist
            if dist > dists[r][c]:
                continue
            dd = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dx, dy in dd:
                rr, cc = r + dx, c + dy
                if rr < 0 or rr >= m or cc < 0 or cc >= n:
                    continue
                cdist = abs(heights[rr][cc] - heights[r][c])
                new_dist = max(dist, cdist)
                if new_dist < dists[rr][cc]:
                    dists[rr][cc] = new_dist
                    heappush(q, (new_dist, (rr, cc)))
        return -1


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
ans = Solution().minimumEffortPath(heights)
print(ans)
