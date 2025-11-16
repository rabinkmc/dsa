from collections import Counter
from typing import List

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        def check_prime(num):
            if num == 1:
                return False
            for i in range(2, num//2 + 1):
                if num % i == 0:
                    return False
            return True

        for num in counter:
            if check_prime(counter[num]):
                return True
        return False
    
    
