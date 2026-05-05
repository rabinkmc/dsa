from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        curr = 0
        ans = 0
        for j in range(n):
            curr += nums[j]
            target = nums[j]
            while target * (j - i + 1) - curr > k:
                curr -= nums[i]
                i += 1
            ans = max(ans, j - i + 1)
        return ans


nums = [1, 2, 4]
k = 5
ans = Solution().maxFrequency(nums, k)
print(ans)
