from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        numbers = [float("-inf")] + nums + [float("-inf")]
        n = len(numbers)
        left = 1
        right = n
        while left <= right:
            m = left + (right - left) // 2
            if numbers[m] > numbers[m - 1] and numbers[m] > numbers[m + 1]:
                return m - 1
            elif numbers[m - 1] > numbers[m]:
                right = m - 1
            else:
                left = m + 1
        return -1


nums = [1, 2, 1, 3, 5, 6, 4]
nums = [3, 2, 4]
ans = Solution().findPeakElement(nums)
print(ans)
