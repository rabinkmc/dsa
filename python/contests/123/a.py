from typing import List
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        def check_valid(a, b, c):
            if a >= b + c:
                return False
            if b >= a + c:
                return False
            if c >= a + b:
                return False
            return True

        is_valid = check_valid(a, b, c)
        if not is_valid:
            return "none"
        if a == b == c:
            return "equilateral"

        if (a == b or a == c or b == c):
            return "isosceles"

        return "scalene"
        
ans = Solution().triangleType(nums=[3, 4, 5])
print(ans)
