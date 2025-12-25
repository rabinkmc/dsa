from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cmax, cmin = 0, 0
        n = len(nums)
        ans_max, ans_min = nums[0], nums[0]
        # idea fucking idea is to find the minimum subarray
        # which is the middle one and subtract that with total, that gives
        # us the other circular subarray

        total = 0
        for i in range(n):
            cmax = max(cmax + nums[i], nums[i])
            ans_max = max(ans_max, cmax)
            cmin = min(cmin + nums[i], nums[i])
            ans_min = min(ans_min, cmin)
            total += nums[i]

        if total == ans_min:
            return ans_max

        return max(ans_max, total - ans_min)


nums = [1, -2, 3, -2]
print(Solution().maxSubarraySumCircular(nums))
