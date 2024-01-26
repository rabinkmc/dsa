class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 1000_000_000 + 7
        result = 1 # holds modular exponentiation
        base = 2
        while n > 0:
            if (n & 1)  == 1:
               result = (result * base) % mod
            n = n >> 1
            base = (base * base) % mod
        return (result - 2) % mod

n = 500000003
print(Solution().monkeyMove(n))

