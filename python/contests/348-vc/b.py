from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i_n = nums.index(n)
        i_1 = nums.index(1)
        ans = (n - 1 - i_n) + i_1
        if i_1 < i_n:
            return ans
        return ans - 1
        
nums = [2,1,4,3]
ans = Solution().semiOrderedPermutation(nums)
print(ans)
