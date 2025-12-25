from typing import List


def merge(left_arr, right_arr):
    i = 0
    j = 0
    m = len(left_arr)
    n = len(right_arr)
    out = []
    while i < m or j < n:
        while i < m and j < n:
            if left_arr[i] <= right_arr[j]:
                out.append(left_arr[i])
                i = i + 1
            else:
                out.append(right_arr[j])
                j = j + 1
        while i < m:
            out.append(left_arr[i])
            i = i + 1

        while j < n:
            out.append(right_arr[j])
            j = j + 1
    return out


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(l, r):
            m = l + (r - l) // 2
            if l == r:
                return [nums[l]]

            left_arr = merge_sort(l, m)
            right_arr = merge_sort(m + 1, r)

            return merge(left_arr, right_arr)

        return merge_sort(0, len(nums) - 1)


nums = [5, 1, 1, 2, 0, 0]

ans = Solution().sortArray(nums)
print(ans)
