from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        ans = 0
        csum = 0
        ans = 0
        lookup = {0: -1}
        for i in range(n):
            csum += nums[i]
            if csum - k  in lookup:
                ans = max(ans, i - lookup[csum - k])
            if csum not in lookup:
                lookup[csum] = i
        return ans

nums = [1,-1,5,-2,3]
k = 3
# nums = [-2, -1, 2, 1]
# k = 1
ans = Solution().maxSubArrayLen(nums, k)
print(ans)
