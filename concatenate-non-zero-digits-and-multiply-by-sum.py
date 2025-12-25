
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total = 0
        num = 0
        tens = 1
        while n:
            digit = n % 10
            if digit:
                num = digit * tens + num
                tens = tens * 10
            total += digit
            n = n // 10
        return num * total

n = 1234003
ans = Solution().sumAndMultiply(n)
print(ans)
