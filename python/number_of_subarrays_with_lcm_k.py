from typing import List
from math import lcm


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr = lcm(curr, nums[j])
                if curr == k:
                    ans += 1
        return ans


nums = [3, 6, 2, 7, 1]
k = 6
ans = Solution().subarrayLCM(nums, k)
print(ans)
