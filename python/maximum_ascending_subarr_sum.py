from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        csum = nums[0]
        ans = csum
        for i in range(len(nums)):
            if nums[i] > nums[i - 1]:
                csum = csum + nums[i]
                ans = max(ans, csum)
            else:
                csum = nums[i]
        ans = max(ans, csum)
        return ans


nums = [10, 20, 30, 5, 10, 50]
ans = Solution().maxAscendingSum(nums)
print(ans)
