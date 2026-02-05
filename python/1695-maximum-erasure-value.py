from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        window = 0
        counter = dict()
        ans = 0
        i = 0
        for j in range(n):
            x = nums[j]
            counter[x] = counter.get(x, 0) + 1
            window += x

            while counter[x] == 2:
                xi = nums[i]
                counter[xi] -= 1
                window -= xi
                i += 1

            ans = max(ans, window)

        return ans


nums = [4, 2, 4, 5, 6]
# nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
ans = Solution().maximumUniqueSubarray(nums)
print(ans)
