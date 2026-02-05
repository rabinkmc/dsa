from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True, key = lambda x: abs(x))
        if n % 2 == 1:
            y = (n + 1) // 2
        else:
            y = n // 2
        ans = 0
        for i in range(y):
            ans += nums[i] * nums[i]
        for i in range(y, n):
            ans -= nums[i] * nums[i]
        return ans
test = [[1,2, 3], [1, -1, 2, -2, 3, -3]]
out = [12, 16]

assert Solution().maxAlternatingSum(test[0]) == 12
assert Solution().maxAlternatingSum(test[1]) == 16
