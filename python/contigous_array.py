from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        csum = 0
        mapper = [-1, 1]
        lookup = {0: -1}
        for i in range(n):
            x = nums[i]
            csum += mapper[x]
            if csum in lookup:
                ans = max(ans, i - lookup[csum])
            if csum not in lookup:
                lookup[csum] = i
        return ans

nums = [0,1,1,1,1,1,0,0,0]
nums = [0, 1]
ans = Solution().findMaxLength(nums)
print(ans)
        
