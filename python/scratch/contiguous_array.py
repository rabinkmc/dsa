from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        csum = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        freq = {0: -1}
        for i in range(n):
            csum += nums[i]
            if csum in freq:
                ans = max(ans, i - freq[csum])
            if csum not in freq:
                freq[csum] = i
        return ans


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
ans = Solution().findMaxLength(nums)
print(ans)
