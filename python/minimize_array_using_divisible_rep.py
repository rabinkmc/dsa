class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        max_value = max(nums)
        exists = [False] * (max_value + 1)
        best_div = list(range(max_value + 1))
        for x in nums:
            exists[x] = True
        for d in range(1, max_value + 1):
            if not exists[d]:
                continue
            for mult in range(d, max_value + 1, d):
                if d < best_div[mult]:
                    best_div[mult] = d
        return sum(best_div[x] for x in nums)


nums = [3, 6, 2]
ans = Solution().minArraySum(nums)
print(ans)
