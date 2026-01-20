class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        prod = 1
        num = n
        while n:
            rem = n % 10
            n = n // 10
            total += rem
            prod *= rem
        print(total)
        print(prod)
        return num % (total + prod) == 0

ans = Solution().checkDivisibility(23)
print(ans)
