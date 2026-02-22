from typing import List
from collections import deque

def bfs(mat, m, n, r, c):
    steps = 0
    queue = deque()
    queue.append((r, c))
    visited = [[False] * n for _ in range(m)]
    visited[r][c] = True
    while queue:
        sz = len(queue)
        for i in range(sz):
            r, c = queue.popleft()
            if mat[r][c] == 0:
                return steps
            dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dx, dy in dd:
                nr, nc = r + dx, c + dy
                if (nr < 0 or nr >= m or nc < 0 or nc >= n):
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                queue.append((nr, nc))
        steps = steps + 1
    return steps


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        out = [[0]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
        return out

mat = [[0,0,0],[0,1,0],[1,1,1]]
ans = Solution().updateMatrix(mat)
print(ans)
        
