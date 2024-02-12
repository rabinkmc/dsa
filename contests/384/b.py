from typing import List
"""
You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.

A subarray nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

    nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
    nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
    nums[i + k + 1] < nums[i + k] if pattern[k] == -1.

Return the count of subarrays in nums that match the pattern.
"""

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def pattern_match(i, k):
            if pattern[k] == 1:
                return nums[i+k+1] > nums[i+k]
            elif pattern[k] == 0:
                return nums[i+k+1] == nums[i+k]
            else:
                return nums[i+k+1] < nums[i+k]
        n = len(nums)
        pn = len(pattern)

        count = 0
        for i in range(n-pn):
            for k in range(pn):
                if not pattern_match(i, k):
                    break
            else:
                count += 1
        return count

ans = Solution().countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])
print(ans)
        
