from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = 0
        sum_counter = {0: 1}
        ans = 0 
        for num in nums:
            psum += num
            if psum - k in sum_counter:
                ans += sum_counter[psum-k]
            sum_counter[psum] = sum_counter.get(psum, 0) + 1
        return ans

ans = Solution().subarraySum(nums = [1,2,3], k = 3)
print(ans)
