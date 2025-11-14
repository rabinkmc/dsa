from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # as long as the current element is greater than the previous element
        # look for the answer on the right
        ans = 0
        m = len(nums) // 2
        n = len(nums)
        l = 0
        r = n  - 1
        while l <= r:
            m = l + (r-l)//2
            if m == 0 or (nums[m] > nums[m-1]):
                ans = m 
                l = m + 1
            else:
                r = m - 1
        return ans

nums = [1,2,1,3,5,6,4]
nums = [1, 2, 3, 1]
nums = [1, 2]
ans = Solution().findPeakElement(nums)
print(ans)
        
