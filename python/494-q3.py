from typing import List


class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        left_map = {}

        def dfs_left(i, curr_xor, length):
            if i == len(left):
                if curr_xor not in left_map or length > left_map[curr_xor]:
                    left_map[curr_xor] = length
                return
            dfs_left(i + 1, curr_xor, length)
            dfs_left(i + 1, curr_xor ^ left[i], length + 1)

        dfs_left(0, 0, 0)
        self.ans = -float("inf")

        def dfs_right(i, curr_xor, length):
            if i == len(right):
                if target ^ curr_xor in left_map:
                    self.ans = max(self.ans, length + left_map[target ^ curr_xor])
                return
            dfs_right(i + 1, curr_xor, length)
            dfs_right(i + 1, curr_xor ^ right[i], length + 1)

        dfs_right(0, 0, 0)
        if self.ans == -float("inf"):
            return -1
        else:
            return n - self.ans


nums = [1, 2, 3]
target = 2
ans = Solution().minRemovals(nums, target)
print(ans)
