from collections import deque


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        visited = set()
        q = deque()
        n, m = m, n
        grid = [[0] * n for _ in range(m)]
        for r, c, color in sources:
            q.append((r, c))
            grid[r][c] = color

        while q:
            sz = len(q)
            adj = {}
            for _ in range(sz):
                r, c = q.popleft()
                dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in dd:
                    rr, cc = r + dx, c + dy
                    if rr < 0 or rr >= m or cc < 0 or cc >= n:
                        continue
                    if grid[rr][cc] != 0:
                        continue
                    if (rr, cc) not in adj or grid[r][c] > adj[(rr, cc)]:
                        adj[(rr, cc)] = grid[r][c]
            for (rr, cc), col in adj.items():
                grid[rr][cc] = col
                q.append((rr, cc))

        return grid


n = 3
m = 3
sources = [[0, 0, 1], [2, 2, 2]]
ans = Solution().colorGrid(n, m, sources)
print(ans)
