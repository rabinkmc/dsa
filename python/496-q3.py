from typing import List


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)
        peaks = [0] * n
        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                continue
            peaks[i] = max(nums[i - 1], nums[i + 1]) - nums[i] + 1
        suffix = [0] * n
        suffix[n - 2] = peaks[n - 2]
        suffix[n - 3] = peaks[n - 3]
        for i in range(n - 3, -1, -1):
            suffix[i] = suffix[i + 2] + peaks[i]
        if n % 2 == 1:
            return suffix[1]
        ans = suffix[1]
        csum = 0
        for i in range(1, n - 1, 2):
            ans = min(ans, csum + suffix[i + 1])
            csum += peaks[i]
        return ans


nums = [5, 2, 1, 4, 3]
nums = [1, 2, 3, 4, 5, 13]
nums = [12, 23, 13, 17, 21, 3]
ans = Solution().minIncrease(nums)
print(ans)
