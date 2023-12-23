from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        left_min = [float('inf')]
        right_min = [float('inf')]
        minl = nums[0]
        minr = nums[len(nums)-1]

        for i in range(1, len(nums)):
            num = nums[i-1]
            if num < minl:
                minl = num
            left_min.append(minl)

        for i in range(len(nums) - 2, -1, -1):
            num = nums[i+1]
            if num < minr:
                minr = num
            right_min.append(minr)

        right_min = right_min[::-1]
        result = -1
        ans = float('inf')
        for left, num, right in zip(left_min, nums, right_min):
            print(left, num, right)
            if num > left and num > right:
                total = num + left + right
                ans = min(ans, total)
                result = ans
        return result


nums = [5, 4, 8, 7, 10,2]
print(Solution().minimumSum(nums))
