from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrayWithKAtMost(nums, k) - self.subarrayWithKAtMost(nums, k - 1)

    def subarrayWithKAtMost(self, nums: List[int], k) -> int:
        i = 0
        ans = 0
        n = len(nums)
        counter = dict()
        total = 0
        for j in range(n):
            x = nums[j]
            counter[x] = counter.get(x, 0) + 1
            while len(counter) > k:
                xi = nums[i]
                counter[xi] -= 1
                if counter[xi] == 0:
                    del counter[xi]
                i = i + 1
            total += j - i + 1
        return total


nums = [1, 2, 1, 2, 3]
k = 2
ans = Solution().subarraysWithKDistinct(nums, k)
print(ans)
