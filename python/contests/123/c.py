from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        psum = [0]
        i = 0 
        j = 0
        n = len(nums)
        for num in nums:
            psum.append(psum[-1] + num)
        ans = 0
        while i < n and j < n:
            while abs(nums[i] - nums[j]) != k:
                j = j + 1
            else:
                ans = max(ans, psum[j+1] - psum[i])
                j = j + 1
                i = j + 1


        return ans
        
nums = [1,2,3,4,5,6]
k = 1
ans = Solution().maximumSubarraySum(nums, k)
print(ans)
