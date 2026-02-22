from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        window = dict()
        csum = 0
        for i in range(k):
            window[nums[i]] = window.get(nums[i], 0) + 1
            csum += nums[i]

        ans = 0
        if len(window) == k:
            ans = csum
        for i in range(k, n):
            prev = nums[i - k]
            curr = nums[i]
            csum = csum + curr - prev
            window[prev] -= 1
            if window[prev] == 0:
                del window[prev]
            window[curr] = window.get(curr, 0) + 1
            if len(window) == k:
                ans = max(ans, csum)
        return ans


nums = [1, 5, 4, 2, 9, 9, 9, 9]
k = 3
ans = Solution().maximumSubarraySum(nums, k)
print(ans)
