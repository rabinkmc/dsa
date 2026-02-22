from typing import List

def check(k, nums):
    count = 0
    for num in nums:
        d =  num // k 
        if num % k != 0:
            d += 1
        count += d
    return count <= k * k

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l = min(nums)
        r = max(nums) * 2
        ans = -1
        while l <= r:
            m = l + (r - l) // 2
            if check(m, nums):
                ans = m 
                r = m - 1
            else:
                l = m + 1
        return ans

nums = [3, 7, 5]
ans = Solution().minimumK(nums)
print(ans)
