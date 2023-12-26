from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = float("inf")
        rsum = 0
        while right < len(nums):
            rsum += nums[right]
            while rsum >= target:
                ans = min(right - left + 1, ans)
                if ans == 1:
                    return 1
                rsum = rsum - nums[left]
                left += 1
            right += 1
        return 1 if ans == float("inf") + 1 else ans


target = 7
nums = [2, 7, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target, nums))
