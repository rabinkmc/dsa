from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        new_nums = []
        sum_count = {0: 1}
        for num in nums:
            new_nums.append(int(num%2==1))
        psum = 0
        ans = 0
        for num in new_nums:
            psum += num
            ans += sum_count.get(psum-k, 0) 
            sum_count[psum] = sum_count.get(psum, 0) + 1
        return ans

ans = Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
print(ans)
