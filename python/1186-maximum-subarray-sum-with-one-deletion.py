from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_sum = zero = one = arr[0]
        for num in arr[1:]:
            one = max(zero, one + num) # take the current zero sum or current_sum + current num i.e we consider not taking a number
            zero = max(zero+num, num) # we consider taking a number 
            max_sum = max(max_sum, one, zero) # we check the current max, current max after considering not taking element , after considering taking just the number
        return max_sum
        
