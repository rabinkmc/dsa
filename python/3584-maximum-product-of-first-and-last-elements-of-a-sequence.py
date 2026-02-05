from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        cmin = 100001
        cmax = -100001
        ans = 0
        for i in range(m, n):
            curr = nums[i]
            last = nums[i - m + 1]
            cmin = min(last, cmin)
            cmax = max(last, cmax)
            ans = max(ans, curr * cmin, curr * cmax)
        return ans


nums = [2, -1, 2, -6, 5, 2, -5, 7]
m = 2
ans = Solution().maximumProduct(nums, m)
print(ans)
