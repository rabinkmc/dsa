from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:

        def check_query(arr):
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        out = []
        for i, j in zip(l, r):
            out.append(check_query(sorted(nums[i : j + 1])))
        return out


nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]
ans = Solution().checkArithmeticSubarrays(nums, l, r)
print(ans)
