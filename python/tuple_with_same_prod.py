from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pairs = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                pairs[nums[i] * nums[j]] += 1
        ans = 0
        for value in pairs.values():
            if value == 1:
                continue
            ans = ans + (value * (value - 1)) * 4
        return ans


nums = [2, 3, 4, 6]
nums = [1, 2, 4, 5, 10]
nums = [2, 3, 4, 6, 8, 12]
ans = Solution().tupleSameProduct(nums)
print(ans)
