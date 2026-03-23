from typing import List

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counter = dict()
        evens = []
        for num in nums:
            if num % 2 == 1:
                continue
            evens.append(num)
            counter[num] = counter.get(num, 0) + 1
        for even in evens:
            if counter[even] == 1:
                return even
        return -1
        
