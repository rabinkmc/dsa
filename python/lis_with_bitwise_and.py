from typing import List
import bisect

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        B = 32
        ans = 0
        for b in range(B):
            tails = []
            for num in nums:
                if num & (1 << b) == 0:
                    continue
                idx = bisect.bisect_left(tails, num)
                if idx >= len(tails):
                    tails.append(num)
                else:
                    tails[idx] = num
            ans = max(ans, len(tails))
        return ans


nums = [5, 4, 7]
nums = [0, 1]
ans = Solution().longestSubsequence(nums)
print(ans)
