from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return False
        pre = 1
        for num in nums:
            pre = pre * num
        if pre != target * target:
            return False
        subsets = []
        self.answer = False
        n = len(nums)
        def search(k):
            if self.answer == True:
                return 
            if k == n:
                pre = 1
                for num in subsets:
                    pre = pre * num
                if pre == target and len(subsets) < len(nums):
                    self.answer = True
                return
            search(k+1)
            subsets.append(nums[k])
            search(k+1)
            subsets.pop()
        search(0)
        return self.answer

        
ans = Solution().checkEqualPartitions([1, 2, 4, 8], target=8)
print(ans)
