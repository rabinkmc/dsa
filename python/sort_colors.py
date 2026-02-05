from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        zidx, tidx = 0, n - 1
        i = 0
        while i <= tidx:
            # if you encounter 2, you swap number with twos_index 
            # if you encounter 0, you swap with zeros_idx
            if nums[i] == 0:
                nums[zidx], nums[i] = nums[i], nums[zidx]
                i += 1
                zidx += 1
            elif nums[i] == 2:
                nums[tidx], nums[i] = nums[i], nums[tidx]
                tidx -= 1
            else:
                i += 1
        print(nums)
nums = [2, 0, 2, 1, 1, 0]
nums = [1,2, 0]
ans = Solution().sortColors(nums)

