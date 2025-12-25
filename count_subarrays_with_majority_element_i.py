from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix_arr = [0] * n
        for i in range(n):
            prefix_arr[i] += (prefix_arr[i - 1] if i - 1 >= 0 else 0) + int(
                nums[i] == target
            )
        ans = 0
        for i in range(n):
            for j in range(i, n):
                count = prefix_arr[j] - (prefix_arr[i - 1] if i - 1 >= 0 else 0)
                if count > (j - i + 1) // 2:
                    ans += 1
        return ans


nums = [5, 4]
target = 5
ans = Solution().countMajoritySubarrays(nums, target)
print(ans)
