from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        for every element, we consider it as the left most element
        and count the numbers that are less than or equal to that
        starting from that point
        """
        count = 0
        n = len(nums)

        # remove the duplicates
        nums = list(set(nums))

        # sort the array for binary search later
        nums.sort()
        for i, left in enumerate(nums):
            right = left + n - 1
            loc = self.bsearch_lte(nums[i:], right)
            count = max(loc + 1, count)
        return n - count

    def bsearch_lte(self, nums, target):
        """
        find numbers that are less than or equal to target

        i do binary search
        pick a middle element:

        There are two possibilities:
        1. The number is lower or equal to the target
        2. The number is higher than the target

        case 1:
        The number is lower or equal to target:
        suppose, the target we were looking for is 7 and below, and
        middle number is 5, now the number that is just lower may
        still be on the right so, the lower bound is the middle
        number itself or higher so the lower bound is now, l = m


        case 2:
        The number is higher than target:
        we are looking for 7, and middle number is 10, so we
        are now certain that the solution is on the left half so
        the higher bound is now, h = m - 1
        """
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo


nums = [1, 2, 3, 4, 6]
nums = [8, 5, 9, 9, 8, 4]
nums = [8, 10, 16, 18, 10, 10, 16, 13, 13, 16]
print(Solution().minOperations(nums))
