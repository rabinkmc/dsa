from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = 0
        for num in nums:
            total = (total + num) % p

        target_remainder = total % p
        if target_remainder == 0:
            return 0

        idx_map = {0: -1}
        csum = 0
        ans = n
        for i in range(n):
            csum = (csum + nums[i]) % p

            remainder_to_find = (csum - target_remainder + p) % p
            if remainder_to_find in idx_map:
                ans = min(ans, i - idx_map[remainder_to_find])

            idx_map[csum] = i

        if ans == n:
            return -1
        return ans


subarr = [8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2]
ans = Solution().minSubarray(subarr, 148)
print(ans)
