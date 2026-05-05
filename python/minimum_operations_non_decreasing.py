class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                ans += nums[i - 1] - nums[i]
        return ans


nums = [3, 3, 2, 1]
ans = Solution().minOperations(nums)
print(ans)
