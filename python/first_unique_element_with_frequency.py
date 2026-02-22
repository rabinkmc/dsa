from typing import List
from collections import Counter, defaultdict

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        counter = Counter(nums)
        freq_table = defaultdict(int)
        for key, count in counter.items():
            freq_table[count] += 1
        for num in nums:
            freq = counter[num]
            if freq_table[freq] == 1:
                return num
        return -1

nums = [20, 10, 30, 30]
ans = Solution().firstUniqueFreq(nums)
print(ans)

