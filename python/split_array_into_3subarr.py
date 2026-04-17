from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + nums[i]

        def rsum(l, r):
            return psum[r + 1] - psum[l]

        return 0


nums = [1, 2, 2, 2, 5, 0]
ans = Solution().waysToSplit(nums)
print(ans)
