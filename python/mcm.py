from functools import lru_cache


def check(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def mcm(p):
    @lru_cache(None)
    def solve(i, j):
        if i == j:
            return 0
        min_cost = float("inf")
        for k in range(i, j):
            cost = solve(i, k) + solve(k + 1, j) + p[i] * p[k + 1] * p[j + 1]
            min_cost = min(cost, min_cost)
        return min_cost

    return solve(0, len(p) - 2)


def min_partition(s):
    @lru_cache(None)
    def solve(i, j):
        if i == j:
            return 0
        if check(s[i : j + 1]):
            return 0
        min_cost = float("inf")
        for k in range(i, j):
            cost = solve(i, k) + solve(k + 1, j) + 1
            min_cost = min(cost, min_cost)
        return min_cost

    return solve(0, len(s) - 1)


# p = [10, 30, 5, 60, 4]
# print(mcm(p))
s = "nitin"
print(min_partition(s))
