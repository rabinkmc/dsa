from typing import List


def reverse(num):
    res = 0
    while num != 0:
        rem = num % 10
        res = res * 10 + rem
        num = num // 10
    return res


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        hash = dict()
        ans = float("inf")
        for i in range(n):
            x = nums[i]
            if x in hash:
                ans = min(ans, i - hash[x])
            key = reverse(x)
            while key % 10 == 0:
                key = key // 10
            hash[key] = i
        if ans == float("inf"):
            return -1
        return ans


nums = [12, 21, 45, 33, 54]
# nums = [120, 21]
# nums = [21, 120]
ans = Solution().minMirrorPairDistance(nums)
print(ans)
