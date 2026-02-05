from typing import List

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        b = 0
        for i in range(n):
            if is_prime(i):
                a += nums[i]
            else:
                b += nums[i]
        return abs(a-b)
        
print(Solution().splitArray([-1, 5, 7, 0]))
