from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rp = [1] * n
        lp = [1] * n
        for i in range(1, n):
            lp[i] = lp[i - 1] * nums[i - 1]
            rp[n - i - 1] = rp[n - i] * nums[n - i]
        return [a * b for a, b in zip(lp, rp)]


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
