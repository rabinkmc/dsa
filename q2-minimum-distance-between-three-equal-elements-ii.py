from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        ans = float("inf")
        for i, num in enumerate(nums):
            indices[num].append(i)
            n = len(indices[num])
            if n >= 3:
                a, b, c = indices[num][n-3:]
                dist = (c - a)*2
                ans = min(ans, dist)
        if ans == float("inf"):
            return -1
        return ans
                
nums = [1, 2, 1, 1, 3]
nums = [1, 2, 3, 1, 1]
print(Solution().minimumDistance(nums))
