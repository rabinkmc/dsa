from typing import List
from collections import Counter


class Solution:
    def bestSum(self, target):
        if target in self.memo:
            return self.memo[target]
        if target == 0:
            return 0
        if target < 0:
            return -1
        ans = float('inf') 
        for num in [2, 3]:
            temp = self.bestSum(target - num)
            if temp == -1:
                continue
            ans = min(ans, 1 + temp)
        self.memo[target] = -1 if ans == float('inf') else ans
        return self.memo[target]

    def minOperations(self, nums: List[int]) -> int:
        self.memo = {}
        counter = Counter(nums)
        min_operations = 0
        for count in counter.values():
            res = self.bestSum(count)
            if res < 0:
                return -1
            min_operations += res
        return min_operations
        
nums = [2,3,3,2,2,4,2,3,4]
nums = [2,1,2,2,3,3]
ans = Solution().minOperations(nums)
print(ans)
