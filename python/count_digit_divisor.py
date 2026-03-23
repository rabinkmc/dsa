class Solution:
    def countDigits(self, num: int) -> int:
        digits = []
        x = num
        while x:
            digits.append(x % 10)
            x = x // 10
        ans = 0
        for digit in digits:
            if num % digit == 0:
                ans += 1
        return ans
