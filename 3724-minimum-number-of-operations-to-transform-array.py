from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 1
        last = nums2[-1]
        dist = 1000000
        for x, y in zip(nums1, nums2[: len(nums1)]):
            x, y = min(x, y), max(x, y)
            ans += y - x
            if x <= last <= y:
                dist = 0
            if dist != 0:
                dist = min(dist, abs(x - last), abs(y - last))
        ans += dist
        return ans


nums1, nums2 = [458, 915], [709, 596, 318]
nums1, nums2 = [2, 8], [1, 7, 3]
# nums1, nums2 = [2], [3, 4]
print(Solution().minOperations(nums1, nums2))
