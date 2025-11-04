from typing import List


class Solution:

    def check_subarray(self, nums, i, k):
        a = i
        for j in range(a + 1, a + k):
            if nums[j] < nums[j - 1]:
                return False

        b = a + k
        for j in range(b + 1, b + k):
            if nums[j] < nums[j - 1]:
                return False
        return True

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            if self.check_subarray(nums, i, k):
                return True
        return False


nums, k = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3
nums, k = [19, 5], 1
print(Solution().hasIncreasingSubarrays(nums, k))
