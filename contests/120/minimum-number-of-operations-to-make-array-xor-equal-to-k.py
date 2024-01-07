from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        highest = max([*nums, k])
        bit = 0
        while highest:
            highest = highest // 2
            bit += 1
        ans = 0
        for i in range(bit): 
            bit_set = sum((num >> i & 1) for num in nums)
            k_bit = (k >> i) & 1
            if k_bit:
                if bit_set % 2 == 0:
                    ans += 1
            else:
                if bit_set % 2 != 0:
                    ans += 1
        return ans

nums = [2,0,2,0]
k = 0

nums = [2, 1, 3, 4]
k = 1

nums = [3, 5, 1,1]
k = 19
ans = Solution().minOperations(nums, k)
print(ans)
        
