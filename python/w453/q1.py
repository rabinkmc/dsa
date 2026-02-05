from typing import List


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        # make 1
        p1 = nums[:]
        p2 = nums[:]
        n = len(nums)
        count1 = k
        for i in range(n - 1):
            if p1[i] == 1:
                continue
            if count1 == 0:
                count1 = -1
                break
            p1[i] *= -1
            p1[i + 1] *= -1
            count1 -= 1
        state1 = count1 > -1 and p1[n - 1] == 1

        # make 2
        count2 = k
        for i in range(n - 1):
            if p2[i] == -1:
                continue
            if count2 == 0:
                count2 = -1
                break
            p2[i] *= -1
            p2[i + 1] *= -1
            count2 -= 1
        state2 = count2 > -1 and p2[n - 1] == -1
        return state1 or state2


nums = [1, -1, 1, -1, 1]
nums = [-1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1]
k = 3
print(Solution().canMakeEqual(nums, k))
