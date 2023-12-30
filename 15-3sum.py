from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer approach
        # first sort the number
        nums.sort()
        n = len(nums) - 1
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n
            target = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append((nums[i] , nums[j] , nums[k]))
                    k = k - 1
                    j = j + 1
                    while j < k and nums[j] == nums[j+1]:
                        j = j + 1
                    while j < k and nums[k] == nums[k-1]:
                        k = k - 1
                elif nums[j] + nums[k] > target:
                    k = k - 1
                else:
                    j = j + 1
        return ans

nums = nums = [-1,0,1,2,-1,-4]
ans = Solution().threeSum(nums)
print(ans)

            

        
