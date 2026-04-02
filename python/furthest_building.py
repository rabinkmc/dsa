from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        for i in range(1, n):
            if heights[i] >= heights[i - 1]:
                continue
        return 0


heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks = 5
ladders = 1
ans = Solution().furthestBuilding(heights, bricks, ladders)
print(ans)
