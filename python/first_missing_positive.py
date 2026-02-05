from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains1 = False
        for i in range(n):
            if nums[i] == 1:
                contains1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not contains1:
            return 1

        for i in range(n):
            index = abs(nums[i])
            if index == n:
                nums[0] = -abs(nums[0])
            else:
                nums[index] = -abs(nums[index])

        print(nums)
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n
        return n + 1


nums = [1, 2, 0]
ans = Solution().firstMissingPositive(nums)
print(ans)
