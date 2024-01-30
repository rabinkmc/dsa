# https://leetcode.com/contest/weekly-contest-320/problems/number-of-unequal-triplets-in-array/
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        total += 1
        return total


ans = Solution().unequalTriplets(nums=[4, 4, 2, 4, 3])
print(ans)
