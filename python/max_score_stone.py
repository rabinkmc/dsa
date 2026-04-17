class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = [a, b, c]
        nums.sort()
        c1, c2, c3 = nums
        if c1 + c2 < c3:
            return c1 + c2
        else:
            return (c1 + c2 + c3) // 2
        return ans


a, b, c = 4, 4, 6
ans = Solution().maximumScore(a, b, c)
print(ans)
