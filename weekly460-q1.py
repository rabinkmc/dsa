from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        median = n - 2
        for _ in range(n // 3):
            total += nums[median]
            median = median - 2
        return total


nums = [2, 1, 3, 2, 1, 3]
ans = Solution().maximumMedianSum(nums)
print(ans)
