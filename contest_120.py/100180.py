from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        ans = -1
        sums = []
        for num in nums:
            total += num
            sums.append(total)

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < sums[i - 1]:
                return sums[i]
        return ans


sides = [1, 12, 1, 2, 5, 50, 3]
print(Solution().largestPerimeter(sides))
