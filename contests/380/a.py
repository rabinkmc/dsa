# problem a
from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_count = max(counter.values())
        ans = 0
        for count in counter.values():
            if count == max_count:
                ans += count
        return ans

nums = [1,2,2,3,1,4]
nums = [1,2,3,4,5]
ans = Solution().maxFrequencyElements(nums)
print(ans)
