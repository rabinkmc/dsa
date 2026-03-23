from typing import List

n = 1000
primes = [True] * (n + 1)
primes[0] = False
primes[1] = False
primes[2] = True

p = 2
while p * p <= n:
    for x in range(p * p, n, p):
        primes[x] = False
    p = p + 1

candidates = []
for i in range(n + 1):
    if primes[i]:
        candidates.append(i)


def distinct_primes(x):
    ans = set()
    for candidate in candidates:
        if x % candidate == 0:
            ans.add(candidate)
            while x % candidate == 0:
                x = x // candidate
                if x == 1:
                    break
    return ans


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        visited = set()
        for x in nums:
            if x in visited:
                continue
            factors = factors | distinct_primes(x)
            visited.add(x)
        return len(factors)


nums = [2, 4, 3, 7, 10, 6]
ans = Solution().distinctPrimeFactors(nums)
print(ans)
