from typing import List
from collections import defaultdict, Counter


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        memo = {}
        def set_bits(num):
            if num in memo:
                return memo[num]
            n  = 0
            temp = num
            while temp:
                temp =  temp /2
                n += 1
            ans = 0
            for i in range(n):
                ans += int((num >> i) & 1)
            memo[num] = ans
            return ans
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    if set_bits(nums[j]) != set_bits(nums[j+1]):
                        return False
                    else:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
        return True
                        


nums = [3,16,8,4,2]
ans = Solution().canSortArray(nums)
print(ans)
