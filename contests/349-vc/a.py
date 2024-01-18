from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        distinct.sort()
        if len(distinct) <= 2:
            return -1
        return distinct[1]

nums = [4,2, 4, 2, 4]
ans = Solution().findNonMinOrMax(nums)
print(ans)
        
