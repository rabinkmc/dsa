from typing import List
from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefix_gcd = []
        mx = nums[0]
        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(gcd(num, mx))
        prefix_gcd.sort()
        l = 0
        r = len(prefix_gcd) - 1
        total = 0
        while l < r:
            total += gcd(prefix_gcd[l], prefix_gcd[r])
            l, r = l + 1, r - 1
        return total

nums = [2, 6, 4]
nums = [3, 6, 2, 8]
ans = Solution().gcdSum(nums) 
print(ans)
