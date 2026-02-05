class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        power = 0
        while n:
            digit = n % 10
            if digit:
                ans += digit * 10**(power)
                power += 1
            n = int(n / 10)
        return ans

for test in [1020030, 104050300200, 1]:
    print(Solution().removeZeros(test))
