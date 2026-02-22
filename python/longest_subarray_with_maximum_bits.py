from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        k = max(nums)
        ans = 1
        curr = 1
        for j in range(1, n):
            if nums[j] == k and nums[j - 1] == k:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 1
        return max(ans, curr)


nums = [3, 3, 3, 3, 3, 3, 3]
print(Solution().longestSubarray(nums))
