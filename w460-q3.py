from typing import List

N = 10**6
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        primes = []
        composites = []
        for i in range(n):
            if i > 0:
                graph[i].append(i - 1)
            if i < n - 1:
                graph[i].append(i + 1)
            if is_prime[nums[i]]:
                primes.append(i)
            else:
                composites.append(i)
        primes.sort(key=lambda x: nums[x])
        for idx in composites:
            x = composites[idx]
            for p in primes:
        return 0
