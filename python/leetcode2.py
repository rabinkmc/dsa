from typing import DefaultDict, List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = DefaultDict(int)
        i = 0
        ans = 0
        for j, num in enumerate(nums):
            counter[num] += 1

            print("top", i, j)
            while counter[num] > k:
                counter[nums[i]] -= 1
                i = i + 1
            ans = max(j - i + 1, ans)

        print(ans)
        return ans


nums = [1, 2, 2, 1, 3]
k = 1
Solution().maxSubarrayLength(nums, k)
