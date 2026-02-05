from typing import Counter, List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        pairs, lo = 0, 0
        for count in counter.values():
            pairs += count // 2
            lo += int(count % 2 == 1)
        return [pairs, lo]
        
