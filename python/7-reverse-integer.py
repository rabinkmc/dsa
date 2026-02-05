class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = (1 << 31) - 1
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            x = x // 10
            if (rev > MAX_INT // 10) or (rev == MAX_INT // 10 and digit > 7):
                return 0
            rev = rev * 10 + digit
        return sign * rev


x = -123
ans = Solution().reverse(x)
print(ans)
