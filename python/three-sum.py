from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        seen = set()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    key = f"{nums[i]},{nums[j]},{nums[k]}"
                    if key not in seen:
                        ans.append([nums[i], nums[j], nums[k]])
                    seen.add(key)
                if total < 0:  # nums[i] is fixed
                    j = j + 1
                else:
                    k = k - 1

        return ans


nums = [-1, 0, 1, 2, -1, -4]
ans = Solution().threeSum(nums)
print(ans)
