from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        temp = sorted(nums[1:])
        b, c = temp[0], temp[1]
        return a + b + c

nums = [10,3,1,1]
nums = [5, 4, 3]
nums = [1, 2, 3, 12]
ans = Solution().minimumCost([10, 3, 1,1])
print(ans)
