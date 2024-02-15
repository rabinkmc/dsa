from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0 
        count = 0
        ans = 0
        for j, num in enumerate(nums):
            if num % 2 == 1:
                count += 1
            while i < len(nums) and count == k:
                # start counting
                ans += 1
                if nums[i] % 2 == 1:
                    count -= 1
                i = i + 1
        return ans

ans = Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
print(ans)
