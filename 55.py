from collections import deque
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for i, num in enumerate(nums):
            graph[i].extend([i + x for x in range(1, num + 1) if i + x < n])

        queue = deque()
        queue.append(0)

        while queue:
            current = queue.popleft()
            if current == n - 1:
                return True
            for next in graph[current]:
                queue.append(next)

        return False


nums = [2, 3, 1, 1, 4]
ans = Solution().canJump(nums)
print(ans)
