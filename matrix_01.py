from typing import List
from collections import deque

def bfs(mat, m, n, queue):
    visited = [[False] * n for _ in range(m)]
    for x, y in queue:
        visited[x][y] = True
    out = [[0]*n for _ in range(m)]
    steps = 0
    while queue:
        sz = len(queue)
        for i in range(sz):
            r, c = queue.popleft()
            if mat[r][c] == 1:
                out[r][c] = steps
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
    return out


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
        return bfs(mat, m, n, queue)

mat = [[0,0,0],[0,1,0],[1,1,1]]
ans = Solution().updateMatrix(mat)
print(ans)
        
