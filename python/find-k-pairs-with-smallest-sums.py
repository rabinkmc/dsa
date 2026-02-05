from typing import List
from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        i = 0
        j = 0
        q = []
        m = len(nums1)
        n = len(nums2)
        visited = set()
        heappush(q, (nums1[i] + nums2[j], (i, j)))
        count = 0
        out = []
        while count < k:
            node = heappop(q)
            i, j = node[1]
            out.append((nums1[i], nums2[j]))
            if i + 1 < m and (i + 1, j) not in visited:
                heappush(q, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heappush(q, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            count += 1
        return out


nums1 = [1, 2, 4, 5, 6]
nums2 = [3, 5, 7, 9]
k = 3
ans = Solution().kSmallestPairs(nums1, nums2, k)
print(ans)
