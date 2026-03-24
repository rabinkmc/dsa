from functools import lru_cache


def target_subset_sum(arr, target):
    @lru_cache(None)
    def dp(i, target):
        if i == len(arr):
            if target == 0:
                return 1
            else:
                return 0
        take = dp(i + 1, target - arr[i])
        skip = dp(i + 1, target)
        return take + skip

    return dp(0, target)


arr = [2, 3, 5, 6, 8, 10]
target = 10

print(target_subset_sum(arr, target))
