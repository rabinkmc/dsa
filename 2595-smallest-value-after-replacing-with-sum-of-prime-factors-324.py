# https://leetcode.com/contest/weekly-contest-324/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_nums_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def prime_total(n):
    primes = prime_nums_generator()
    curr = next(primes)
    total = 0
    while n > 1:
        while n % curr == 0:
            print(curr)
            n = n // curr
            total += curr
        else:
            curr = next(primes)
    return total


class Solution:
    def smallestValue(self, n: int) -> int:
        num = n
        while not is_prime(num):
            ptot = prime_total(num) 
            if ptot == num:
                return num
            num = ptot
        return num

ans = Solution().smallestValue(n=4)
print(ans)
