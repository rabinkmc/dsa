from collections import Counter
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        right_count = Counter(nums)
        left_count = Counter()
        total = 0
        for i in range(n):
            num = nums[i]
            right_count[num] -= 1
            total += left_count[num * 2] * right_count[num * 2]
            left_count[num] += 1
        return total


nums = [8, 4, 2, 8, 4]
print(Solution().specialTriplets(nums))
