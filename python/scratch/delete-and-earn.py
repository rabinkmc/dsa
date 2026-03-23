from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numbers = sorted(set(nums))
        n = len(numbers)
        dp = [0] * n
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + num
        dp[0] = counter[numbers[0]]
        if n == 1:
            return dp[0]
        if numbers[1] - numbers[0] > 1:
            dp[1] = dp[0] + counter[numbers[1]]
        else:
            dp[1] = max(dp[0], counter[numbers[1]])
        for i in range(2, n):
            csum = counter[numbers[i]]
            if numbers[i] - numbers[i - 1] == 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + csum)
            else:
                dp[i] = dp[i - 1] + csum
        return dp[n - 1]


nums = [3, 5, 2]
nums = [1, 1, 1, 2, 4, 5, 5, 5, 6]
ans = Solution().deleteAndEarn(nums)
print(ans)
