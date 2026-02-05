from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        for i in range(1, len(nums)):
            highest = [lis[j] for j, num in enumerate(nums) if num < nums[i]]
            lis[i] = 1 + max(highest, default=0)
        return lis[-1]


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
