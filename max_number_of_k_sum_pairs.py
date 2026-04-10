from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        while l < r:
            if nums[l] + nums[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] >= k:
                r -= 1
            else:
                l += 1
        return ans


nums = [1, 2, 3, 4]
k = 5
# nums = [3, 1, 3, 4, 3]
# k = 6
ans = Solution().maxOperations(nums, k)
print(ans)
