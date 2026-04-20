from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        if m > 6 * n or n > 6 * m:
            return -1
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
            m, n = n, m
        i = 0
        j = n - 1
        ops = 0
        nums1.sort()
        nums2.sort()
        while s2 > s1:
            # just pick a number that is the highest
            if (j < 0) or (i < m and 6 - nums1[i] > nums2[j] - 1):
                s1 += 6 - nums1[i]
                i += 1
            else:
                s2 -= nums2[j] - 1
                j -= 1
            ops += 1

        return ops


# nums1 = [1, 2, 3, 4, 5, 6]
# nums2 = [1, 1, 2, 2, 2, 2]
nums1 = [6, 6]
nums2 = [1]
ans = Solution().minOperations(nums1, nums2)
print(ans)
