from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        psum = [nums[0]]
        for num in nums[1:]:
            psum.append(psum[-1] + num)
        print(psum)
        n = len(nums)
        ans = []
        div = 2 * k + 1
        for i in range(n):
            if i < k:
                ans.append(-1)
            elif n - 1 - i < k:
                ans.append(-1)
            else:
                l = i - k
                r = i + k
                total = psum[r] - psum[l - 1] if l >= 1 else psum[r]
                ans.append(total // div)
        return ans


nums = [100000]
k = 0
print(Solution().getAverages(nums, k))
