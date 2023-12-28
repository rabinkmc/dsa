from collections import defaultdict
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        can_reach = 0
        jumps = 0
        while r < len(nums) -1:
            jumps += 1
            for i in range(l, r+1):
                can_reach = max(can_reach, i + nums[i])

            l, r = r+1, can_reach
        return jumps



nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
