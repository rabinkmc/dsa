from collections import defaultdict


def subarray_sum_equals_k(nums, k):
    csum = 0
    psum_count = defaultdict(int)
    psum_count[0] = 1
    ans = 0
    for num in nums:
        csum += num
        ans += psum_count[csum - k]
        psum_count[csum] += 1
    return ans


assert subarray_sum_equals_k([1, 2, 1, 2], 3) == 3
