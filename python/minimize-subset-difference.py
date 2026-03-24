from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        S = sum(nums)
        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target] == True:
                break
        for j in range(target, -1, -1):
            if dp[j] == True:
                return S - 2 * j
        return -1


nums = [3, 9, 7, 3]
print(Solution().minimumDifference(nums))
