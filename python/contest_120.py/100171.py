from typing import List

nums = [1, 2, 3, 4]
nums = [6, 5, 7, 8]


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                flag = True
                prev = float("-inf")
                for k in range(len(nums)):
                    if k in range(i, j + 1):
                        continue
                    if nums[k] <= prev:
                        flag = False
                        break
                    prev = nums[k]
                if flag:
                    ans += 1

        return ans


ans = Solution().incremovableSubarrayCount(nums)
print(ans)
