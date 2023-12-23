from typing import List
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        def dfs(i,target, path=[]):
            if target == 0:
                return 1
            if target < 0:
                return float('inf')
            if i >= len(nums):
                return float('inf')
        
            left = 1 + dfs(i+1, target-nums[i], [*path, nums])
            right = dfs(i+1, target, path)
            return min(left, right)
            
        
        ans = dfs(0,target)
        return ans


print(Solution().lengthOfLongestSubsequence([1,2,3,4], 9))

        
