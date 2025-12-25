from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        po = [0]*n
        pe = [0]*n
        so = [0]*n
        se = [0]*n
        odd_sum = 0
        even_sum = 0
        for i in range(n):
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
            pe[i] = even_sum
            po[i] = odd_sum

        # to the right odd and even sums are 
        # exchanged
        odd_sum = 0
        even_sum = 0
        for i in range(n-1, -1, -1):
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
            so[i] = even_sum
            se[i] = odd_sum

        ans = 0
        for i in range(n):
            reven = se[i+1] if i + 1< n  else 0
            rodd = so[i+1] if i + 1 < n else 0
            leven = pe[i-1] if i - 1 > -1 else 0
            lodd = po[i-1] if i - 1 > -1 else 0
            if reven + leven == rodd + lodd:
                ans += 1
        return ans

nums = [1, 2, 1, 2, 3, 1]
ans = Solution().waysToMakeFair(nums)
print(ans)
        
