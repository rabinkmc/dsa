class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            if max(nums[: i + 1]) - min(nums[i:]) <= k:
                return i
        return -1


nums = [5, 0, 1, 4]
k = 3
ans = Solution().firstStableIndex(nums, k)
print(ans)
