from typing import List
from collections import deque


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        q = deque()
        # r, c, side_steps
        q.append((2, 0, 0))
        n = len(obstacles)
        visited = set()
        while q:
            r, c, steps = q.popleft()
            if c == n - 1:
                return steps
            if obstacles[c + 1] == r:
                for i in [1, 2, 3]:
                    if i == r:
                        continue
                    if obstacles[c] == i:
                        continue
                    if (i, c) in visited:
                        continue
                    q.append((i, c, steps + 1))
                    visited.add((i, c))
            else:
                while c + 1 < n and obstacles[c + 1] != r:
                    c = c + 1
                if (r, c) in visited:
                    continue
                q.append((r, c, steps))
                visited.add((r, c))
        return -1


obstacles = [0, 1, 2, 3, 0]
ans = Solution().minSideJumps(obstacles)
print(ans)
