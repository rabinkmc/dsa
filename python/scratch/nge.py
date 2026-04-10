from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        hash = dict()
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            hash[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        n1 = len(nums1)
        out = []
        for num in nums1:
            out.append(hash[num])
        return out


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
ans = Solution().nextGreaterElement(nums1, nums2)
print(ans)
