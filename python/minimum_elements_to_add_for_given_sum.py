from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        if s == goal:
            return 0
        if s < goal:
            diff = goal - s
            ops = diff // limit
            if diff % limit != 0:
                ops += 1
            return ops
        diff = s - goal
        ops = diff // limit
        if diff % limit != 0:
            ops += 1
        return ops


nums = [1, -1, 1]
limit = 3
goal = -4

nums = [1, -10, 9, 1]
limit = 100
goal = 0
ans = Solution().minElements(nums, limit, goal)
print(ans)
