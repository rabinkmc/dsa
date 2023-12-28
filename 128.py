from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        ans = 0
        nums.sort()
        for num in nums:
            prev = num - 1
            hash[num] = 1 + hash[prev]
            ans = max(hash[num],ans)
        return ans
        

nums = [0,3,7,2,5,8,4,6,0,1]
ans = Solution().longestConsecutive(nums)
print(ans)

