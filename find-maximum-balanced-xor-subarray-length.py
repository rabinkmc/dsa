from typing import List

# 11
# 01
# 11
# 10
# 00


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        csum = 0
        n = len(nums)
        seen = {(0, 0): -1}
        ans = 0
        oc = 0
        ec = 0
        for j in range(n):
            if nums[j] % 2 == 0:
                ec += 1
            else:
                oc += 1
            csum = csum ^ nums[j]
            hash = (csum, ec - oc)
            if hash in seen:
                i = seen[hash]
                ans = max(ans, j - i)
            else:
                seen[hash] = j
        return ans


nums = [3, 1, 3, 2, 0]
nums = [3, 2, 8, 5, 4, 14, 9, 15]
# nums = [0]

ans = Solution().maxBalancedSubarray(nums)
print("\n", ans)
