from typing import List


def rev(num):
    rv = 0
    while num:
        rv = rv * 10 + (num % 10)
        num = num // 10
    return rv


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numbers = set(nums)
        for num in nums:
            numbers.add(rev(num))
        return len(numbers)
