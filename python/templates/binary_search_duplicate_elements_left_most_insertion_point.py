import bisect


def fn(arr, target):
    left = 0
    right = len(arr) - 1

    ans = 0
    while left <= right:
        mid = left + (left - right) // 2
        if target <= arr[mid]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    # left is the insertion point
    return ans
