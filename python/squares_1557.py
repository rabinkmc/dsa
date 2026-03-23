from typing import List
from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for num in nums1:
            hash1[num * num] += 1
        for num in nums2:
            hash2[num * num] += 1
        for i in range(n2 - 1):
            for j in range(i + 1, n2):
                ans += hash1[nums2[i] * nums2[j]]
        for i in range(n1 - 1):
            for j in range(i + 1, n1):
                ans += hash2[nums1[i] * nums1[j]]
        return ans


nums1 = [7, 4]
nums2 = [5, 2, 8, 9]
ans = Solution().numTriplets(nums1, nums2)
print(ans)
