from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        # start from the end
        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

nums = [2,3,1,1,4]
ans = Solution().canJump(nums)
print(ans)
        
