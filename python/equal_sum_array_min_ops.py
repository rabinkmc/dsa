from typing import List


def ops_add(c, diff):
    # first fill up the ones
    ops = 0
    for i in range(1, 6):
        if c[i] == 0:
            continue
        mult = 6 - i
        if diff > c[i] * mult:
            diff = diff - c[i] * mult
            ops += c[i]
        else:
            if diff < mult:
                return ops + 1
            ops += diff // mult
            if diff % mult != 0:
                ops += 1
            return ops
    return ops


def ops_sub(c, diff):
    ops = 0
    for i in range(6, 1, -1):
        if c[i] == 0:
            continue
        mult = i - 1
        if diff > c[i] * mult:
            diff = diff - c[i] * mult
            ops += c[i]
        else:
            ops += diff // mult
            if diff % mult != 0:
                ops += 1
            return ops
    return 0


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        if m > 6 * n or n > 6 * m:
            return -1
        # try all possibilities of sum
        s_min, s_max = 0, 0
        if m < n:
            s_max = m * 6
            s_min = n
        else:
            s_max = n * 6
            s_min = m

        c1 = [0] * 7
        c2 = [0] * 7
        s1 = 0
        for num in nums1:
            c1[num] += 1
            s1 += num
        s2 = 0
        for num in nums2:
            c2[num] += 1
            s2 += num
        ans = float("inf")
        for s in range(s_min, s_max + 1):
            if s < s1:
                ops1 = ops_sub(c1, s1 - s)
            else:
                ops1 = ops_add(c1, s - s1)

            if s < s2:
                ops2 = ops_sub(c2, s2 - s)
            else:
                ops2 = ops_add(c2, s - s2)
            ans = min(ans, ops1 + ops2)
        return ans  # type: ignore


nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [1, 1, 2, 2, 2, 2]
nums1 = [6, 6]
nums2 = [1]
ans = Solution().minOperations(nums1, nums2)
print(ans)
