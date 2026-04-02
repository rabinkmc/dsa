from math import comb
from functools import lru_cache

MOD = 1_000_000_007
MAX_N = 100_001

fact = [1] * MAX_N
for i in range(1, MAX_N):
    fact[i] = fact[i - 1] * i % MOD

inv_fact = [1] * MAX_N
inv_fact[MAX_N - 1] = pow(fact[MAX_N - 1], MOD - 2, MOD)
for i in range(MAX_N - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD


def comb_mod(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        if k >= n:
            return 0
        lmax = min(k, pos)
        total = 0
        ## the thing is there are 'pos' positions to the left
        ## if pos == 3, then that means we have 3 positions to the left
        ## and n = 5, then that means we have n - 1 - pos to the
        ## right
        ## so we will always have this fixed

        ## now the only the thing that we have to do
        ## now suppose 0 person is on the left, then there are k - 0 to the right
        ## suppose 1 person is on the left, then there are k - 1 to the right
        ## suppose 2 person is on the left, then there are k - 2 to the right
        ## so it is the summation of perm_left * perm_right over lidx 0 to k
        MOD = 1000_000_007
        for i in range(lmax + 1):
            j = k - i
            if j > n - 1 - pos:
                continue
            lp = comb_mod(pos, i)
            rp = comb_mod(n - 1 - pos, k - i)
            total += lp * rp % MOD
        return (total * 2) % MOD


data = [
    [3, 1, 0],
    [3, 2, 1],
    [2, 0, 1],
    [3, 0, 2],
]
for n, pos, k in data:
    ans = Solution().countVisiblePeople(n, pos, k)
    print(ans)
