from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while k >= 0:
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        print(nums1)


nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
print(Solution().merge(nums1, m, nums2, n))
