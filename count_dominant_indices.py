from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > sum(nums[i:]) / len(nums[i:]):
                ans += 1
        return ans

nums = [5, 4, 3]
ans = Solution().dominantIndices(nums)
print(ans)

                

