from typing import List


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        ec = 0
        for num in nums1:
            if num % 2 == 0:
                ec += 1
        if ec == len(nums1):
            return True

        oc = 0
        for num in nums1:
            if num % 2 == 1:
                oc += 1
            else:
                if oc == 0:
                    return False
        return True


nums1 = [1, 4, 7]
ans = Solution().uniformArray(nums1)
print(ans)
