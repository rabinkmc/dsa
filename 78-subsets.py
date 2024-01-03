from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(1 << n): 
            temp = []
            for j in range(n):
                bit = (i >> j) & 1
                if bit:
                    temp.append(nums[j])
            result.append(temp)
        return result



nums = [1, 2, 3]
ans = Solution().subsets(nums)
print(ans)

