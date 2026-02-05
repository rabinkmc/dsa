from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter_dict = Counter(nums)
        n = len(nums)
        result = []
        def dfs(comb, counter):
            if len(comb) == n:
                result.append(comb[:])
                return
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    dfs(comb,counter)
                    comb.pop()
                    counter[num] += 1
        dfs([], counter_dict)
        return result

nums = [1,1,2]
ans = Solution().permuteUnique(nums)
print(ans)

