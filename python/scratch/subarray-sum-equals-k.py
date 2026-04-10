from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        n = len(nums)
        csum = 0
        ans = 0
        for j in range(n):
            csum += nums[j]
            if csum - k in freq:
                ans += freq[csum - k]
            freq[csum] = freq.get(csum, 0) + 1
        return ans


nums = [1, 1, 1]
k = 2
ans = Solution().subarraySum(nums, k)
print(ans)
