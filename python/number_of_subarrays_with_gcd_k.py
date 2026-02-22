from typing import List
from math import gcd


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            curr = nums[i]
            for j in range(i, n):
                curr = gcd(curr, nums[j])
                if curr == k:
                    ans += 1
        return ans
