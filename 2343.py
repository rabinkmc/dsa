import enum
from typing import List


def f(nums, k, trim):
    out = []
    for i in range(len(nums)):
        out.append((nums[i][-trim:], i))
    out.sort()
    return out[k-1][1]

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for k, trim in queries:
            ans.append(f(nums, k, trim))

        return ans
        

nums = ["102","473","251","814"]
queries = [[1,1],[2,3],[4,2],[1,2]]
ans = Solution().smallestTrimmedNumbers(nums, queries)
print(ans)
