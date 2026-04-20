from typing import List
from bisect import bisect_left


def closest(arr, target):
    idx = bisect_left(arr, target)
    if idx == 0:
        return arr[0]
    if idx == len(arr):
        return arr[-1]

    before = arr[idx - 1]
    after = arr[idx]
    if target - before < after - target:
        return before
    else:
        return after


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        diffs = []
        psum = 0
        n = len(nums1)
        for x, y in zip(nums1, nums2):
            diff = abs(x - y)
            diffs.append(diff)
            psum += diff
        ans = psum
        nums1.sort()
        max_gain = 0
        for i in range(n):
            y = nums2[i]
            tmp = closest(nums1, y)
            old_diff = diffs[i]
            new_diff = abs(tmp - y)
            max_gain = max(max_gain, old_diff - new_diff)
        return (psum - max_gain) % 1_000_000_007


nums1 = [1, 7, 5]
nums2 = [2, 3, 5]
ans = Solution().minAbsoluteSumDiff(nums1, nums2)
print(ans)
