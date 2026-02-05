from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones == n:
            return 0

        if ones:
            return n - ones

        n = len(nums)
        MAX = n + 1
        size = MAX
        for i in range(n - 1):
            hcf = nums[i]
            for j in range(i + 1, n):
                hcf = gcd(hcf, nums[j])
                if hcf == 1:
                    size = min(size, j - i + 1)
                    break
        if size == MAX:
            return -1
        return n - 1 + (size - 1)


nums = [2, 10, 6, 14]
# nums = [1, 2]
print(Solution().minOperations(nums))
