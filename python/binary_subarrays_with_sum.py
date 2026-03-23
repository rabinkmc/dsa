from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        csum = 0
        freq = {0: 1}
        ans = 0
        for x in nums:
            csum += x
            target = csum - goal
            if target in freq:
                ans += freq[target]
            freq[csum] = freq.get(csum, 0) + 1
        return ans

nums = [1,0,1,0,1]
goal = 2
ans = Solution().numSubarraysWithSum(nums, goal)
print(ans)
        
