from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        queue = deque([(sr, sc)])
        h = len(image)
        w = len(image[0])
        seen = {(sr, sc)}
        new_image = [[0] * w for _ in range(h)]

        for rr in range(h):
            for cc in range(w):
                new_image[rr][cc] = image[rr][cc]

        while queue:
            cr, cc = queue.popleft()
            new_image[cr][cc] = color
            dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in dd:
                nr, nc = cr + dr, cc + dc
                if nr < 0 or nr > h - 1 or nc < 0 or nc > w - 1:
                    continue

                if image[sr][sc] != image[nr][nc]:
                    continue
                if (nr, nc) in seen:
                    continue

                queue.append((nr, nc))
                seen.add((nr, nc))
        return new_image


solution = Solution()

ans1 = solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
assert ans1 == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

ans2 = solution.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)
assert ans2 == [[0, 0, 0], [0, 0, 0]]
