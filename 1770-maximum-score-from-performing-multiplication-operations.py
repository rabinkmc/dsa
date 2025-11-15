from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        memo = dict()

        def dp(i, left):
            if i == m:
                return 0
            if (i, left) in memo:
                return memo[(i, left)]

            right = n - 1 - (i - left)
            mult = multipliers[i]

            lcurr = mult*nums[left]
            rcurr = mult*nums[right]
            ans = max(lcurr + dp(i+1, left+1), rcurr + dp(i+1, left))
            memo[(i, left)] = ans

            return ans
        return dp(0, 0)

nums= [1, 2, 3]
multipliers = [3, 2, 1]
print(Solution().maximumScore(nums, multipliers))

