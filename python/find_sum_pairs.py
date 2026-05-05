from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.c1 = dict()
        self.c2 = dict()

        for num in nums1:
            self.c1[num] = self.c1.get(num, 0) + 1

        for num in nums2:
            self.c2[num] = self.c2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        key = self.nums2[index]
        self.c2[key] -= 1
        self.nums2[index] = key + val
        self.c2[key + val] = self.c2.get(key + val, 0) + 1

    def count(self, tot: int) -> int:
        ans = 0
        for key in self.c1:
            if tot - key in self.c2:
                ans += self.c1[key] * self.c2[tot - key]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
