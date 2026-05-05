class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out = []
        for i in range(n):
            if i == 0 or i == n - 1:
                out.append(nums[i])
                continue
            if nums[i] > max(nums[:i]) or nums[i] > max(nums[i + 1 :]):
                out.append(nums[i])
        return out


nums = [1, 2, 4, 2, 3, 2]
ans = Solution().findValidElements(nums)
print(ans)
