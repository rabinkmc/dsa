class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n <= 2:
            return 1
        return n - 1
        
