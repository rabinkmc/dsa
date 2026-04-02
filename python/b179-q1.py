class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        MAX = 200
        ans = MAX
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (nums[i] == 1 and nums[j] == 2) or (nums[i] == 2 and nums[j] == 1):
                    ans = min(ans, j - i)
        if ans == MAX:
            return -1
        return ans


nums = [1, 0, 0, 2, 0, 1]
ans = Solution().minAbsoluteDifference(nums)
print(ans)
