from typing import List

class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lsum = sum(nums)
        rprod = 1
        for i in range(n-1, -1, -1):
            lsum = lsum - nums[i]
            if lsum == rprod:
                return i
            if lsum < rprod:
                break
            rprod = rprod * nums[i]

        return -1

nums = [2, 1, 2]
ans = Solution().smallestBalancedIndex(nums)
print(ans)
        
