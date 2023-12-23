from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if zero1 == 0:
            if sum2 + zero2 > sum1:
                return -1
        if zero2 == 0:
            if sum1 + zero1 > sum2:
                return -1

        return max(sum1 + zero1, sum2 + zero2)


nums1 = [9, 5]
nums2 = [15, 12, 5, 21, 4, 26, 27, 9, 6, 29, 0, 18, 16, 0, 0, 0, 20]
nums1 = [3, 2, 0, 1, 0]
nums2 = [6, 5, 0]
# nums1 = [0, 0, 10, 10, 12, 0, 13, 6, 0, 2, 10]
# nums2 = [24, 5, 12, 22]
# nums1 = [8, 13, 15, 18, 0, 18, 0, 0, 5, 20, 12, 27, 3, 14, 22, 0]
# nums2 = [29, 1, 6, 0, 10, 24, 27, 17, 14, 13, 2, 19, 2, 11]

print(Solution().minSum(nums1, nums2))
