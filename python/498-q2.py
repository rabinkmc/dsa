class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        curr = nums[0]
        for i in range(n):
            curr = max(nums[i], curr)
            prefix[i] = curr

        curr = nums[n - 1]
        for i in range(n - 1, -1, -1):
            curr = min(nums[i], curr)
            suffix[i] = curr

        for i in range(n):
            if prefix[i] - suffix[i] <= k:
                return i
        return -1


nums = [5, 0, 1, 4]
k = 3
ans = Solution().firstStableIndex(nums, k)
print(ans)
