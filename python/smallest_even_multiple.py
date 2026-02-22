class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2


n = 5
ans = Solution().smallestEvenMultiple(n)
