from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        self.success = success
        self.potions = potions
        p_size = len(potions)
        res = []
        for spell in spells:
            target = success / spell
            print(target)
            loc = self.bsearch(potions, target)
            if loc != -1:
                res.append(p_size - loc)
            else:
                res.append(0)

        return res

    def bsearch(self, nums, target):
        i = 0
        j = len(nums) - 1
        result = -1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                result = m
                j = m - 1

        return result


spells = [3, 1, 2]
potions = [8, 5, 8]
success = 16


# print(bsearch(6))
print(Solution().successfulPairs(spells, potions, success))
