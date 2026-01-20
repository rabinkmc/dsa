from typing import List


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        tmp = [[0] * k for _ in range(k)]
        for r in range(x, x + k):
            for c in range(y, y + k):
                tmp[r - x][c - y] = grid[r][c]
        tmp = tmp[::-1]
        for r in range(x, x + k):
            for c in range(y, y + k):
                grid[r][c] = tmp[r - x][c - y]
        return grid
