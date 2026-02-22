from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        def check_incr():
            for i in range(1, n):
                if nums[i] < nums[i-1]:
                    return False
            return True
        def check_decr():
            for i in range(1, n):
                if nums[i] > nums[i-1]:
                    return False
            return True
        return check_incr() or check_decr()

nums = [3, 2, 2, 3]
ans = Solution().isMonotonic(nums)
print(ans)

        
