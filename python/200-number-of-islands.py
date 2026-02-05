from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        h = len(grid)
        w = len(grid[0])
        nodes = []

        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    nodes.append((i, j))

        moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(node):
            r, c = node
            for dr, dc in moves:
                rr = r + dr
                cc = c + dc
                if rr < 0 or rr >= h or cc < 0 or cc >= w or grid[rr][cc] == "0":
                    continue
                next_node = (rr, cc)
                if next_node not in visited:
                    visited.add(next_node)
                    dfs(next_node)

        count = 0
        for node in nodes:
            if node not in visited:
                count += 1
                visited.add(node)
                dfs(node)
        return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

ans = Solution().numIslands(grid)
print(ans)
