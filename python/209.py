from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        csum = 0
        i = 0
        j = 0
        n = len(nums)
        ans = n + 1
        for j in range(n):
            x = nums[j]
            csum += x
            while csum >= target:
                length = j - i + 1

                if ans > length:
                    ans = length

                csum -= nums[i]
                i += 1
        if ans == n + 1:
            return 0
        return ans


target = 10
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(Solution().minSubArrayLen(target, nums))
